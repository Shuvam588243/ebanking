from django.urls import path
from user import views

urlpatterns = [
    path('',views.index,name="User Home Page"),
    path('Dashboard/',views.dashboard,name="User Dashboard"),
    path('Transfer/',views.transfer,name="User Dashboard"),
    path('MyProfile/',views.my_profile,name="User Profile"),
    path('DepositMoney/',views.deposit,name="User Profile"),
    

]