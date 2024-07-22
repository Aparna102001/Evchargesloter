from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    # add any other fields relevant to your application
    def save(self, *args, **kwargs):
        self.user.wallet.balance -= self.amount
        self.user.wallet.save()
        super(Transaction, self).save(*args, **kwargs)



from django.utils import timezone

class Slot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} {self.start_time} - {self.end_time} ({'Available' if self.available else 'Booked'})"

