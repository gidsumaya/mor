from django.contrib import admin
from .models import Mobile, Sms


class MobileAdmin(admin.ModelAdmin):
    list_display = ('mobile_owner', 'mobile_number')


class SmsAdmin(admin.ModelAdmin):
    list_display = ('rainfall_id', 'mobile_id')


admin.site.register(Mobile, MobileAdmin)
admin.site.register(Sms, SmsAdmin)