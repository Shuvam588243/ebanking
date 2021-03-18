from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('AboutUs/',views.aboutus,name="about"),
    path('ContactUs/',views.contactus,name="contact"),
    path('Service/',views.service,name="service"),
    path('User/',include('user.urls')),
    path('Clerk/',include('clerk.urls'),name="clerk_login"),
]


