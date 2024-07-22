from django.contrib import admin
from .models import Wallet, Transaction,Slot

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')

@admin.register(Transaction)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date')


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'end_time', 'available')
    list_filter = ('date', 'available')
    search_fields = ('date', 'start_time', 'end_time')
    ordering = ('date', 'start_time')