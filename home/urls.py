from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'), 
    path('signin/',views.signin,name='signin'),
    path('userslot/',views.userslot,name='userslot'),
    path('staffportal/',views.staffportal,name='staffportal'),
    path('add_money/', views.add_money, name='add_money'),
    path('wallet/', views.wallet, name='wallet'),
    path('pay/', views.pay, name='pay'),
    path('staffsignup/',views.staffsignup,name='staffsignup'), 
    path('staffsignin/',views.staffsignin,name='staffsignin'),
    path('slot_list/',views.slot_list,name='slot_list'),
    path('booking_confirm/<int:slot_id>/',views.booking_confirm,name='booking_confirm'),
    path('slot_detail/',views.book_slot,name='slot_detail'),

    
    
]
