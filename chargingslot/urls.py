from django.urls import path
from . import views
urlpatterns=[
    path('',views.chargingslot,name='chargingslot')
    
]
