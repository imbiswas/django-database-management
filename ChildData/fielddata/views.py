from __future__ import unicode_literals
from .models import *
from .forms import *
from .serializers import ChildSerializer, LoginSerializer
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse,Http404,HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


#for adding record of a new child
def add_data(request):
	if not request.user.has_perm('poll.change_poll'):
		return HttpResponseRedirect('/')
	else:

		if request.method == 'POST':
			forms = FieldForm(request.POST,request.FILES,)
			if forms.is_valid():
				form_data = forms.save(commit=False)
				form_data.filled_by = request.user
				form_data.save()
				messages.success(request, f'New data added successfully!')
				return HttpResponseRedirect('/')
		else:
			forms = FieldForm()
		context_dict = {'forms': forms}
		return render (request,'childForm.html',context_dict)

#updating record of existing child
def update(request,id=None):
	if not request.user.has_perm('poll.change_poll'):
		return HttpResponseRedirect('/')
	else:
		instance = get_object_or_404(Child_Entry,Child_Id=id)
		forms = FieldForm(request.POST,request.FILES, instance=instance)
		if forms.is_valid():
			instance = forms.save(commit=False)
			instance.save()
			messages.success(request, f'Data updated successfully!')
			return HttpResponseRedirect('/gallery')
		context = {'forms':forms,
		"instance" : instance,
		"Child_name" : instance.Child_name,
		}
		return render (request,'childForm.html',context)

#deleting the child
def delete(request,id=None):
	if not request.user.has_perm('poll.change_poll'):
		return HttpResponseRedirect('/')
	else:
		instance = get_object_or_404(Child_Entry,Child_Id=id)
		instance.delete()
		messages.success(request, f'Data deleted successfully!')
		return HttpResponseRedirect('/gallery')

#API for child data
class ApiDataView(viewsets.ModelViewSet):
	queryset = Child_Entry.objects.all()
	serializer_class = ChildSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

#Login api which sends token for auth
class LoginView(APIView):
	def post(self,request):
		serializer = LoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		django_login(request,user)
		token, created = Token.objects.get_or_create(user=user)
		return Response({"token":token.key , 'id': token.user_id},status=200)

#Logout Api which clears sessions
class LogoutView(APIView):
	authentication_classes=(TokenAuthentication,)
	def post(self,request):
		django_logout(request)
		return Response(status=204)