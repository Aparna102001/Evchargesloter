from django.shortcuts import render
from .models import slotpoints


def chargingslot(request):
    slots =slotpoints.objects.all()
    
   
    return render(request,'chargingslot.html',{'slots':slots})
    