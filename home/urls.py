from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contactus", views.contactus, name='Contact Us'),
    path("signup",views.signup,name='signup' ),
    path("retailers",views.retailers,name='retailers')
]
