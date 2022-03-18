from rest_framework import serializers
from appointment import models
# from doctorSignup.models import DoctorDetail
from doctorSignup.models import DoctorsData
from services.models import AddService
from userSignup.models import UserData, UserDetail


class appointSerial(serializers.ModelSerializer):
    class Meta:
        model = models.AppointDetail
        fields = '__all__'


class DoctorData(serializers.ModelSerializer):
    class Meta:
        model = DoctorsData
        fields = ['FirstName', 'LastName']

class patientData(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['FirstName', 'LastName']

class PurposeData(serializers.ModelSerializer):
    class Meta:
        model = AddService
        fields = ['services']


class appointUserSerial(serializers.ModelSerializer):
    Doctor = DoctorData()
    purpose = PurposeData()

    class Meta:
        model = models.AppointDetail
        fields = ['id', 'purpose', 'Doctor', 'patient', 'date', 'times', 'price']


class appointDoctorSerial(serializers.ModelSerializer):
    patient = patientData()
    purpose = PurposeData()

    class Meta:
        model = models.AppointDetail
        fields = ['id', 'purpose', 'patient', 'date', 'times', 'price']
