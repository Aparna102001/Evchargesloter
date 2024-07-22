from django.urls import path
from . import views
urlpatterns=[
    path('',views.bookingslot,name='bookingslot'),
    path('confirmation/',views.confirmation,name='confirmation'),
    
]
