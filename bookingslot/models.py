from django.db import models
from datetime import datetime,date


# Create your models here.
class mybookingslot(models.Model):
    fullname = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    adress = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    time = models.TextField(max_length=10)

    
    
    def __str__(self):
      return self.fullname



    