from django.db import models


class Mobile(models.Model):
    mobile_owner = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=11)


class Sms(models.Model):
    rainfall = models.ForeignKey('device.Rainfall', on_delete=models.CASCADE)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

