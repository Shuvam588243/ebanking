from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.models import User

# Create your views here.
def index(request):
    context = {}

    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']


        try:
            user = User.objects.get(user_name = uname , password = pwd)

        except Exception:
            context['message'] = "Invalid User Credentials"
            return render(request,"home_dashboard.html",context)
        else:
             if user:
                 return redirect('user_dashboard',id=user.id)


        



    return render(request,"home_dashboard.html",{})

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



