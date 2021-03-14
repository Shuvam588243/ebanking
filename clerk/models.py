from django.db import models

# Create your models here.
class Clerk(models.Model):

    cfname = models.CharField(max_length=100)
    cuname = models.CharField(max_length=100)
    cphone = models.IntegerField(max_length=100)
    cemail = models.CharField(max_length=100)
    caddress = models.TextField(max_length=100)
    cpassword = models.CharField(max_length=100)
    
def __str__(self):
    return self.cfname + "" + self.cuname