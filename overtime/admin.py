from django.contrib import admin

from .models import Overtime
# Register your models here.

@admin.register(Overtime)
class OvertimeAdmin(admin.ModelAdmin):
    list_display = ('noreg','date_in','date_out')
    list_filter = ('date_in','date_out')