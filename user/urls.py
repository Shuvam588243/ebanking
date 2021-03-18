from django.urls import path
from user import views

urlpatterns = [
    path('Dashboard/<id>',views.dashboard,name="user_dashboard"),
    path('MyProfile/<id>',views.my_profile,name="profile"),
    path('DepositMoney/<id>',views.deposit,name="deposit"),
    path('TransferMoney/<id>',views.transfer,name="money_transfer"),
    
    

]
