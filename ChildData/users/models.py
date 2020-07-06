from django.db import models
from django.contrib.auth.models import User
from .choices import *
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_picture = models.ImageField(upload_to='profile',default='profile/user.PNG',null=True, blank=True,)
    Gender = models.CharField(max_length=32,choices=Gender_choice,null=True, blank=True)
    address= models.CharField(max_length=50,null=True, blank=True)
    phone = models.DecimalField(decimal_places=0,max_digits=10,null=True, blank=True)
    Date_of_Birth = models.DateField(null=True, blank=True)
    Nationality = models.CharField(max_length=10,null=True, blank=True)
    Religion = models.CharField(max_length=15,choices=religion_choices,null=True, blank=True)


    def __str__(self):
        return '%s'%(self.user)
