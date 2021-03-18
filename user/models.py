from django.db import models

# Create your models here.
class User(models.Model):

    user_name = models.CharField(max_length=50)
    fullname = models.CharField(max_length=120)
    address = models.TextField(max_length=200)
    user_phone = models.CharField(max_length=10)
    user_email = models.CharField(max_length=90)
    account_number = models.CharField(max_length=20)
    current_balance = models.CharField(max_length=10)
    password = models.CharField(max_length=20) 

    def __str__(self):
         return self.user_name + " " + self.user_email
         