"""
URL configuration for Django_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from My_App import views
from pull_request import views as vie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MyPlc.home,name='Home'),
    path('aboutMe/',views.MyPlc.aboutMe,name='aboutMe'),
    path('contact/',views.MyPlc.contact,name='contact'),
    path('certifiaction/',views.MyPlc.certification,name='certification'),
    path('thisweb/',views.MyPlc.thisweb,name='thisweb'),
    path('pr/',vie.pr,name='pr'),
    path('rds_onboarding/',views.MyPlc.rds_onboarding,name='rds_onboarding'),
    path('services/',views.MyPlc.services,name='services'),
    path('index/',views.MyPlc.index,name='index'),
]
