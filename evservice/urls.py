from django.urls import path
from . import views
urlpatterns=[
    path('',views.evservice,name='evservice'),
    
]
