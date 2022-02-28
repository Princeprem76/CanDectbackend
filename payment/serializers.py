from rest_framework import serializers
from payment import models


class paymentSerial(serializers.ModelSerializer):
    class Meta:
        model = models.payments
        fields = '__all__'


class serviceSerial(serializers.ModelSerializer):
    class Meta:
        model = models.AddService
        fields = ['services']


class paymentDisplaySerial(serializers.ModelSerializer):
    service = serviceSerial()

    class Meta:
        model = models.payments
        fields = ['price', 'payment_method', 'user', 'service', 'Date']
