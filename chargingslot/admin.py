from django.contrib import admin

# Register your models here.
from .models import slotpoints
class SlotpointsAdmin(admin.ModelAdmin):
    list_display=('pumpname','location','time')
   
admin.site.register(slotpoints,SlotpointsAdmin)
