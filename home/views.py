
from smtplib import SMTPResponseException
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is homepage")
def contactus(request):
    return HttpResponse("This is contact us page")
def signup(request):
    return render(request, 'signup.html')
def retailers(request):
    return render(request, 'retailers.html')
    


    



