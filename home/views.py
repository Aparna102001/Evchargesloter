from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Wallet,Transaction
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm, AddMoneyForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
from .models import Slot


def index(request):
    return render(request,'index.html')



def signup(request):
    if request.method=='POST':
       
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password1')
        user=User.objects.create_user(username,email,pass1)
        user.save()
    
        print(username,email,pass1,pass2)
        messages.success(request,"account created successfully!!")
        return redirect('signin')
    else:
       messages.error(request,"account creation unsuccessfull!!")

    return render(request,'signup.html') 

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.error(request,"LOGIN SUCCESSFULLY")
            return redirect('userslot')
            print(username,pass1)
        else:
           messages.error(request,"USERID OR PASSWORD IS ERROR!!!!!")  
   
         
    return render(request,'signin.html')
 
def userslot(request):
    slots = Slot.objects.filter(available=True).order_by('date', 'start_time')
    context = {'slots': slots}
    return render(request, 'userslot.html', context)
   

def staffportal(request):
   return render(request,'staffportal.html')




def add_money(request):
    if request.method == 'POST':
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            wallet = request.user.wallet
            wallet.balance += amount
            wallet.save()
            return redirect('wallet')
        
    else:
        form = AddMoneyForm()
    return render(request, 'add_money.html', {'form': form})




@login_required
def wallet(request):
    balance = request.user.wallet.balance
    return render(request, 'wallet.html', {'balance': balance})



def pay(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)
    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['payamount']
            if wallet.balance >= amount:
                wallet.balance -= amount
                wallet.save()
                return redirect('wallet')
            else:
                form.add_error(None, "Insufficient funds in wallet.")
    else:
        form = PaymentForm()

    return render(request, 'pay.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required





def staffsignin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.error(request,"LOGIN SUCCESSFULLY")
            return redirect('staffportal')
            print(username,pass1)
        else:
           messages.error(request,"USERID OR PASSWORD IS ERROR!!!!!")  
    return render(request,'staffsignin.html')

def staffsignup(request):
    if request.method=='POST':
       
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password1')
        user=User.objects.create_user(username,email,pass1)
        user.save()
    
        print(username,email,pass1,pass2)
        messages.success(request,"account created successfully!!")
        return redirect('staffsignin')
    else:
       messages.error(request,"account creation unsuccessfull!!")

    
    return render(request,'staffsignup.html')
    






def slot_list(request):
    # get all available slots
    slots = Slot.objects.filter(available=True).order_by('date', 'start_time')
    context = {'slots': slots}
    return render(request, 'slot_list.html', context)

def book_slot(request, slot_id):
    # get the selected slot
    slot = get_object_or_404(Slot, pk=slot_id)

    if request.method == 'POST':
        # check if the selected slot is still available
        if slot.available:
            # update the slot to booked status
            slot.available = False
            # reduce the slot duration by 1 hour
            slot.end_time = datetime.strptime(slot.end_time, '%H:%M:%S') - timedelta(hours=1)
            slot.save()
            # redirect to confirmation page
            return HttpResponseRedirect(reverse('booking_confirm', args=(slot_id,)))
        else:
            # display error message
            context = {'error_message': 'The selected slot is no longer available.'}
            return render(request, 'slot_detail.html', context)

    else:
        # display the slot details and booking form
        context = {'slot': slot}
        return render(request, 'slot_detail.html', context)

from django.shortcuts import render, redirect
from .models import Slot
from .forms import SlotForm

def booking_confirm(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    if request.method == 'POST':
        slot.available = False
        slot.save()
        return redirect('slot_list')
    return render(request, 'booking_confirm.html', {'slot': slot})
