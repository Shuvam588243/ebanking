from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
    context = {}

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user =  authenticate(username=username, password=password)

        if user :
            print("Login")
            request.session['username'] = user.user_namepython 
        else:
            print("Invalid")

       
    return render(request,"index.html",{})


        





def dashboard(request,id):

    
    user = User.objects.get(id=id)
    
    context = {}

    context['mydata'] = user

    return render(request,"dashboard.html",context)
   
    
    


def transfer(request,id):
    user = User.objects.get(id=id)
    
    context = {}

    context['mydata'] = user

    return render(request,"transfer_money.html",context)

def my_profile(request,id):

    user = User.objects.get(id=id)
    
    context = {}
    

    

    

    context['mydata'] = user

    if request.method=='POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        acnumber = request.POST['acnum']
        curbal = request.POST['balance']
        password = request.POST['password']

        print(username,fullname,address,phone,email,acnumber,curbal,password)

        user.user_name = username
        user.fullname = fullname
        user.address = address
        user.user_phone = phone
        user.user_email = email
        user.account_number = acnumber
        user.current_balance = curbal
        user.password = password

        user.save()

        return render(request,"dashboard.html",context)
        

    return render(request,"my_profile.html",context)



def deposit(request,id):
    user = User.objects.get(id=id)
    
    context = {}

    context['mydata'] = user

    return render(request,"deposit.html",context)




def logout(request):

    try:
        del request.session['username']
        del request.session['id']
    except :
        pass
    return redirect('home')