import datetime
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    now=datetime.datetime.now()
    html="<html><body><h2>Now time is %s.</h2></body></html>"%now
    return HttpResponse(html)
def welcome(request):
    return HttpResponse("Welcome to Django Class")
def intro(request):
    return HttpResponse("This is an IT institution")
def emobilis(request):
    return HttpResponse("eMobilis mobile Technology Institute")
def Home(request):
    return render(request,'home.html')
def Services(request):
    return render(request,'Services.html')
def Contactus(request):
    return render(request,'Contact us.html')
def Products(request):
    return render(request,'Products.html')
def Partners(request):
    return render(request,'Partners.html')
