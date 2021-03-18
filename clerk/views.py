from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.models import User
from .models import Clerk



# Create your views here.
def dashbaord(request,id):

    clerk = Clerk.objects.get(id=id)

    context = {}

    context['data'] = clerk

    return render(request,"clerk_dashboard.html",context)


def login(request):
    context = {}

    if request.method == 'POST':
        cname = request.POST['username']
        pwd = request.POST['password']

        try:

            userc = Clerk.objects.get(cuname = cname, cpassword = pwd)
        
        except Exception:
            print("Invalid")
            context['error'] = "Invalid Crentials"
            return render(request,'clerk_index.html',context)

        else:
          return redirect('clerk_dashbaord',id=userc.id)
        
    return render(request,'clerk_index.html',{})

def create_user(request):
    context = {}

    if request.method=='POST':

        username = request.POST['username']
        fullname = request.POST['fullname']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        acnumber = request.POST['acnum']
        curbal = request.POST['balance']
        password = request.POST['password']



        user = User.objects.create(user_name = username, fullname = fullname, address = address, user_phone = phone,
        user_email = email,  account_number = acnumber, current_balance = curbal, password = password)
        user.save()

        

        


    return render(request,"create_user.html",{})



def search(request):

    context = {}

    if request.method == 'POST':
        name = request.POST['username']

        user = User.objects.get(user_name=name)

        





    return render(request,"search_user.html",{})


def update(request,uname):
    print(uname)
    user = User.objects.get(user_name=uname)
    print(user)
    return render(request,"update_user.html",{})