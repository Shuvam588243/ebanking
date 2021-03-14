from django.shortcuts import render
from django.http import HttpResponse
from user.models import User


# Create your views here.
def dashbaord(request):
  return render(request,"clerk_dashboard.html",{})

def login(request):
    mytext = "<h1> Clerk Login Here </h1>"
    return HttpResponse(mytext)

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

        if user:
            context['mydata'] = user
            print(user.user_name)
            return render(request,"update_user.html",context)
        else:
            print("Bhag")





    return render(request,"search_user.html",{})


def update(request):
    pass