from django.contrib import admin
from .models import Rainfall


# Register your models here.

class RainfallAdmin(admin.ModelAdmin):
    list_display = ('level', 'amount', 'timestamp')


admin.site.register(Rainfall, RainfallAdmin)