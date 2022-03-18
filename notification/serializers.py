from rest_framework import serializers
from notification import models
from doctorSignup.models import DoctorsData



class NotifySerial(serializers.ModelSerializer):
    class Meta:
        model = models.notifyDetail
        fields = '__all__'

class DoctorNameSerial(serializers.ModelSerializer):
    class Meta:
        model = DoctorsData
        fields = ['FirstName','LastName']



class NotifyUserSerial(serializers.ModelSerializer):
    Doctor_Name = DoctorNameSerial()
    class Meta:
        model = models.notifyDetail
        fields = ['Doctor_Name','Date','Mesage']
