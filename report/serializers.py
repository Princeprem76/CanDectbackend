from rest_framework import serializers
from report import models


class ReportSerial(serializers.ModelSerializer):
    class Meta:
        model = models.ReportDetail
        fields = '__all__'
