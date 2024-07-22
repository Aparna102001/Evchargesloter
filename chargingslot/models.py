from django.db import models

# Create your models here.
class slotpoints(models.Model):
   pumpname = models.CharField(max_length=255)
   location = models.CharField(max_length=255)
   time = models.IntegerField()
