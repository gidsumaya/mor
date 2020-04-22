from rest_framework import serializers
from .models import Rainfall


class RainfallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rainfall
        fields = ('id', 'level', 'amount', 'timestamp')
