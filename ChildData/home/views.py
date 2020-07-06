from django.shortcuts import render
from fielddata.models import Child_Entry
from django.http import HttpResponse

#renders home page
def index (request):
    return render(request,'home/index.html')

#renders gallery page
def gallery (request):
    queryset = Child_Entry.objects.all()
    context = {
        "photos":queryset,
    }
    return render(request,'home/gallery.html',context)

    
#child view profile page
def childId(request,child_id):
    
    queryset = Child_Entry.objects.filter(Child_Id=child_id)
    context = {
        "details":queryset,
    }
    return render(request,'home/child.html',context)