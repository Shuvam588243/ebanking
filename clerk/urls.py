from django.urls import path
from clerk import views

urlpatterns = [
    path('',views.login,name="clerk_login"),
    path('Dashboard/<id>',views.dashbaord,name="clerk_dashbaord"),
    path('CreateUser/',views.create_user,name="create_user"),
    path('SearchUser/',views.search,name="search_user"),
    path('UpdateUser/',views.update,name="update_user"),
    path('Logout/',views.logout,name="logout"),
    path('Showuserbyname/<uname>',views.byname,name="showuserbyname"),

]
