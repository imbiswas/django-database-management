from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from fielddata.models import Child_Entry
from .models import Adoption
from django.urls import reverse

# view for child adopt
@login_required
def adopt(request,id):
    queryset = Child_Entry.objects.filter(Child_Id=id)
    context = {
        "details":queryset,
    }
    return render(request,'payment/adopt.html',context)

#save payment information and adopt information
def pay(request,id=None): 
    if request.method == 'POST':
        # print(id)
        current_user = request.user
        # print (current_user.id)
        
        data=request.POST
        # print(data['total'])
        adopted = Child_Entry.objects.get(Child_Id=id)
        if adopted.adopt:
            return HttpResponse("Oops!!! the child is already adopted.")
        else :
            adopted.adopt = True
            adopted.save()
            edu = adopted.education
            clo = adopted.clothing
            tot = float(edu)+float(clo)
            total = tot+0.13*tot
            print(edu,clo,tot,total)
            action = Adoption.objects.create(user=current_user,Child_id=id,total=total,Child_name=data['name'],Gender=data['gender'],link=data['link'])

            if action:
                return render(request,'payment/pay.html')
            else:
                return HttpResponse("Error Occured!!!")