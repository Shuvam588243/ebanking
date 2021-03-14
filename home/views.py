from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    mytext="<h1> Home Page </h1>"
    return HttpResponse(mytext)

def aboutus(request):
    mytext="<h1> About Us Page </h1>"
    return HttpResponse(mytext)

def contactus(request):
    mytext="<h1> Contact Us Page </h1>"
    return HttpResponse(mytext)


def service(request):
    mytext="<h1> SErvices Page </h1>"
    return HttpResponse(mytext)


def userlogin(request):
    mytext="<h1> User Login </h1>"
    return HttpResponse(mytext)



