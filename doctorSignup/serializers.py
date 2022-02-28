from rest_framework import serializers
from doctorSignup import models


class DoctorSignUpSerial(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetail
        fields = '__all__'


class DoctorDataSerial(serializers.ModelSerializer):
    class Meta:
        model = models.DoctorsData
        fields = ['id', 'FirstName', 'LastName','Doctoremail']

class DoctorupdatedetailSerial(serializers.ModelSerializer):

    class Meta:
        model = models.DoctorsData
        fields = ['Doctoremail', 'age', 'address', 'phone']


class DoctorIDSerial(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetail
        fields = ['id']
