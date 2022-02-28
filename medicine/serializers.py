from rest_framework import serializers
from medicine import models


class MedicineSerial(serializers.ModelSerializer):
    class Meta:
        model = models.medicineDetail
        fields = '__all__'
