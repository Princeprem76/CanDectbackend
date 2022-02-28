from rest_framework import serializers
from services import models


class ServicesSerial(serializers.ModelSerializer):
    class Meta:
        model = models.AddService
        fields = '__all__'
