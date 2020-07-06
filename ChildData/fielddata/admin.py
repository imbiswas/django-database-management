from django.contrib import admin
from .models import *
# Register your models here.
class photo(admin.ModelAdmin):
    list_display=["Child_name","timestamp"]
    class Meta:
        model=Child_Entry

admin.site.register(Child_Entry,photo)
