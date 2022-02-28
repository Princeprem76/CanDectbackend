from rest_framework import serializers
from userSignup import models


class UserSignUpSerial(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetail
        fields = '__all__'


class UserpwSerial(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetail
        fields = ['email', 'password']


class UserhasDataSerial(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetail
        fields = ['is_Verified', 'has_data']


class UserSignUpDataSerial(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetail
        fields = ['id', 'email']

class UserdetaSerial(serializers.ModelSerializer):
    class Meta:
        model = models.UserData
        fields = '__all__'

class Useremaildata(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetail
        fields = ['email']


class UserReportSerial(serializers.ModelSerializer):
    useremail = Useremaildata()

    class Meta:
        model = models.UserData
        fields = ['useremail', 'id', 'FirstName', 'LastName']


class UserupdatedetailSerial(serializers.ModelSerializer):
    class Meta:
        model = models.UserData
        fields = ['useremail', 'age', 'address', 'phone']
