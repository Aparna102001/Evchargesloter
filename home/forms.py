from django import forms

class PaymentForm(forms.Form):
    payamount = forms.DecimalField(max_digits=10, decimal_places=2)

class AddMoneyForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

from django import forms
from .models import Slot

class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ('date', 'start_time', 'end_time')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }