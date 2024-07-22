from django.contrib import admin
from .models import mybookingslot
class mybookingslotAdmin(admin.ModelAdmin):
    list_display=('fullname','location','adress',"date","time")

admin.site.register(mybookingslot,mybookingslotAdmin)