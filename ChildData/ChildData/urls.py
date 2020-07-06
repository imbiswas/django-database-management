"""ChildData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include
from home import views as homeview
from django.conf.urls import url

urlpatterns = [
    path("",homeview.index, name='index'),
    path('paypal',include('paypal.standard.ipn.urls')),
    path("gallery",homeview.gallery, name='gallery'),
    # path("child",homeview.child_profile, name='child_profile'),
    path("child/<child_id>",homeview.childId, name='childId'),
    path('admin/', admin.site.urls),
    path('field/', include('fielddata.urls')),
    path('users/', include('users.urls')),
    path('adopt/', include('payment.urls')),
    
    url(r'^rest-auth/', include('rest_auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)