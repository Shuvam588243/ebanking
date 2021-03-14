from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('AboutUs/',views.aboutus,name="home"),
    path('ContactUs/',views.contactus,name="home"),
    path('Service/',views.service,name="home"),
    path('User/',include('user.urls')),
    path('Clerk/',include('clerk.urls')),
]

