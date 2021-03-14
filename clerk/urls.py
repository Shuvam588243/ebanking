from django.urls import path
from clerk import views

urlpatterns = [
    path('',views.dashbaord,name="Clerk Dashbaord"),
    path('Login/',views.login,name="User Login Page"),
    path('CreateUser/',views.create_user,name="Create User"),

]