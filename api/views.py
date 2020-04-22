from device.models import Rainfall
from device.serializers import RainfallSerializer
from rest_framework import viewsets
from main.models import Mobile, Sms
from main.serializers import MobileSerializer, SmsSerializer


class MobileView(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class SmsView(viewsets.ModelViewSet):
    queryset = Sms.objects.all()
    serializer_class = SmsSerializer


class RainfallView(viewsets.ModelViewSet):
    queryset = Rainfall.objects.all()
    serializer_class = RainfallSerializer


