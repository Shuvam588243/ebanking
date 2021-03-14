from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    context = {}

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user =  authenticate(username=username, password=password)

        if user :
            print("Login")
        else:
            print("Invalid")

       
    return render(request,"index.html",{})


        





def dashboard(request):
    return render(request,"dashboard.html",{})


def transfer(request):
    return render(request,"transfer_money.html",{})

def my_profile(request):
    return render(request,"my_profile.html",{})

def deposit(request):
    return render(request,"deposit.html",{})



