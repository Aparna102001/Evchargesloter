from django import forms
from .models import mybookingslot

class Mydata(forms.ModelForm):
    class Meta:
        model = mybookingslot
        fields = ["fullname","location","adress","date","time"]
        labels = {"fullname": "fullname","location":"location","adress":"adress","date":"date","time":"time"}