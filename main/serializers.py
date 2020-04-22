from rest_framework import serializers
from .models import Mobile, Sms


class MobileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mobile
        fields = ('id', 'mobile_owner', 'mobile_number')


class SmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sms
        fields = ('id', 'rainfall_id', 'mobile_id', 'timestamp')
