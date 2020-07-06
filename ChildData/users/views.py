from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import *
from fielddata.models import Child_Entry
from payment.models import Adoption
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse

# New user signup
def signup(request):#for user signup
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Your account has been created successfully!')
            form.save()
            return redirect('signin')
            
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

#view user profile
@login_required
def profile(request):#for user profile
    #get child data from field data
    datas = Child_Entry.objects.all()
    #get current user
    current_user = request.user

    #get all data from adoption
    adopt_list = Adoption.objects.filter(user=current_user)

    #for my entry
    my_entry = Child_Entry.objects.filter(filled_by=current_user)    
    
    # for instance for edit profile
    instance= get_object_or_404(Profile,user=current_user)
    

    #for edit email, name and password
    if request.method =='POST':
        
        editprofile = EditProfileForm(request.POST,instance=request.user)
        if editprofile.is_valid():
            editprofile.save()
            return redirect('/users/profile')

        
    else:
        editprofile = EditProfileForm(instance=request.user)
        context = {
            'profile':editprofile,
            'datas':datas,
            'adopt_list':adopt_list,
            'instance':instance,
            'my_entry' : my_entry
            }
        return render(request,'users/profile.html',context)

#change login password
@login_required   
def change_password(request):
    if request.method =='POST':
        form=PasswordChangeManualForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/users/profile')
        else:
            return redirect('/users/change-password')
    else:
        form = PasswordChangeManualForm(user=request.user)
        context = {
            'form':form,
        }
        return render(request,'users/password.html',context)

#update user details 
@login_required
def updateuser(request):
    current_user = request.user
    if request.method== 'POST':
        data = request.POST
        edit = Profile.objects.get(user=current_user)
        edit.Gender = data['Gender']
        edit.address = data['address']
        edit.phone = data['phone']
        edit.Date_of_Birth = data['Date_of_Birth']
        edit.Nationality = data['Nationality']
        edit.Religion = data['Religion']
        edit.save()
        return redirect(request.META['HTTP_REFERER'])
    return HttpResponse("Error Occured!!!")


# def profile_pic(request):
#     current_user = request.user
#     if request.method == 'POST':
#         data = request.POST
#         edit = Profile.objects.get(user=current_user)
#         print(data)
#         # edit.Profile_picture=data.get('profilepic')
#         edit.save()
#     return HttpResponse("Error Occured!!!")

#add a new staff user with permission by admin
def new_user(request):#for user add
    if not request.user.has_perm('poll.change_poll'):
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = NewUserRegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, f'New account has been created successfully!')
                form.save()
                return redirect('new_user')
            
        else:
            form = NewUserRegisterForm()
        return render(request,'users/new_user.html',{'form':form})
    