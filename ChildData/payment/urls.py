from django.urls import path,include
from . import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('ids/<id>', views.adopt, name='adopt'),
    path('pay/<id>', views.pay, name='pay'),
]