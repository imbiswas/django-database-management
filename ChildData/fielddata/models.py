from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from .choices import *
# Create your models here.
class Child_Entry(models.Model):
    
    #Details Section
    Child_name = models.CharField(max_length=32)
    Child_Id = models.AutoField(primary_key=True)
    Gender = models.CharField(max_length=32,choices=Gender_choice)
    photo = models.ImageField(null=False,blank=False)
    Description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

    #Basic Details
    Date_of_Birth = models.DateField()
    Blood_Group = models.CharField(max_length=5,choices=blood_choices)
    Birth_place = models.CharField(max_length=50)
    Nationality = models.CharField(max_length=50)
    Mother_Tongue = models.CharField(max_length=50)
    Religion = models.CharField(max_length=50,choices=religion_choices)
    National_Identity_card_type = models.CharField(max_length=50)
    National_ID_Card_Number=models.CharField(max_length=50)

    #Contact details
    Permanent_Address = models.CharField(max_length=25)
    Present_Address = models.CharField(max_length=25)
    City = models.CharField(max_length=50)
    Zip = models.CharField(max_length=10)
    State = models.CharField(max_length=20,choices=state_choices)
    Country = models.CharField(max_length=50)
    Phone = models.DecimalField(max_digits=10, decimal_places=0)
    Mobile = models.DecimalField(max_digits=10, decimal_places=0)
    Email = models.EmailField()

    #Parent details
    Fathers_Name = models.CharField(max_length=25)
    Fathers_Contact_Number = models.DecimalField(max_digits=10, decimal_places=0)
    fathers_Profession = models.CharField(max_length=50)
    Fathers_National_ID_Card_type = models.CharField(max_length=50)
    Fathers_National_ID_Card_Number = models.CharField(max_length=50)

    Mothers_Name = models.CharField(max_length=50)
    Mothers_Contact_Number = models.DecimalField(max_digits=10, decimal_places=0)
    Mothers_Profession = models.CharField(max_length=50)
    Mothers_National_ID_Card_type = models.CharField(max_length=50)
    Mothers_National_ID_Card_Number = models.CharField(max_length=50)

    Local_Parents_Name = models.CharField(max_length=50)
    Relationship = models.CharField(max_length=50)
    Local_Parents_Contact_Number = models.DecimalField(max_digits=10, decimal_places=0)
    Local_Parents_Profession = models.CharField(max_length=50)
    Local_Parents_National_ID_Card_type = models.CharField(max_length=50)
    Local_Parents_National_ID_Card_Number = models.CharField(max_length=50)
    Income = models.DecimalField(max_digits=10, decimal_places=2)

    #Schooling details
    School_Name = models.CharField(max_length=50)
    Grade = models.CharField(max_length=10,choices=grade_choices)
    clothing = models.DecimalField(decimal_places=0,max_digits=10)
    education = models.DecimalField(decimal_places=0,max_digits=10)

    adopt = models.BooleanField(default=False,null=True, blank=True)
    filled_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '%s'%(self.Child_name)
    class Meta:
      ordering = ["-timestamp"] 