from django.urls import path,include

from . import views
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken import views as rest_views
router=routers.DefaultRouter()
router.register('data',views.ApiDataView)
urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^add/$',views.add_data,name='add_form'),
    path('api',include(router.urls)),
    path('api-token-auth',rest_views.obtain_auth_token, name='api_token'),
    path('edit/<id>',views.update, name='update'),
    path('delete/<id>',views.delete, name='delete'),
    path('api/login',views.LoginView.as_view(), name='apilogin'),
    path('api/logout',views.LogoutView.as_view(), name='apilogout'),
    
]