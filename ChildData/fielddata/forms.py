from django import forms
from .models import *


#for form of child data 
class FieldForm(forms.ModelForm):
    class Meta:
        model = Child_Entry
        exclude = ('filled_by',)
        # fields = '__all__'
        


