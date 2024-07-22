from django.shortcuts import render
from .models import mybookingslot
from .forms import Mydata

from django.contrib import messages



def bookingslot(request):
    if request.method == 'POST':
        form = Mydata(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user_id = request.user.id
            
            booking.save()
            form.save()
            messages.success(request, 'Your booking has been confirmed!')
            return render(request, 'confirmation.html', {'booking': booking})
    else:
        form = mybookingslot()
    return render(request, 'bookingslot.html', {'form': form})

def confirmation(request):
   confirm=mybookingslot.objects.all()
   return render(request,'confirmation.html',{'confirm':confirm})