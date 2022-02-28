from rest_framework import serializers
from notification import models



class NotifySerial(serializers.ModelSerializer):
    class Meta:
        model = models.notifyDetail
        fields = '__all__'

class DoctorNameSerial(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetail
        fields = ['FirstName','LastName']



class NotifyUserSerial(serializers.ModelSerializer):
    Doctor_Name = DoctorNameSerial()
    class Meta:
        model = models.notifyDetail
        fields = ['Doctor_Name','Date','Mesage']
