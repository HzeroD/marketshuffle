from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
path('', views.Home.as_view(), name='home'),
path('about/', views.about, name='about'),
path('accounts/signup/', views.signup, name='signup')

]