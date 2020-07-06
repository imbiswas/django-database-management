from rest_framework import serializers
from .models import *
from rest_framework import exceptions
from django.contrib.auth import authenticate

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child_Entry
        fields = ("__all__")

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self,data):
        username = data.get("username","")
        password = data.get("password","")
        email = data.get("email","")

        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    if user.is_staff :
                        data["user"]=user
                    else:
                        msg = "You dont have permission."
                        raise exceptions.ValidationError(msg)
                
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        elif email and password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    if user.is_staff :
                        data["user"]=user
                    else:
                        msg = "You dont have permission."
                        raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username or email and password."
            raise exceptions.ValidationError(msg)
        return data