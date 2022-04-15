from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import CreateUserForm, CreateUserDetailForm, AdminLog
from .models import UserDetail, UserData
import random
from .utils import Util
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSignUpSerial, UserSignUpDataSerial, UserReportSerial, UserhasDataSerial, \
    UserpwSerial, UserupdatedetailSerial, UserdetaSerial
import django.db


# Create your views here.
@api_view(['POST'])
def send_code(request):
    data = request.data
    code = random.randint(1000, 9999)
    email_subject = 'Verification Code'
    email_body = 'Hi user,' + '\n Welcome to Can-Dect! \n Please use the below Code to verify your email \n Code: {} '.format(
        code)
    data = {'email_body': email_body,
            'email': data['email'], 'subject': email_subject}
    Util.send_email(data)
    return Response(code)


@api_view(['POST'])
def send_password_code(request):
    data = request.data
    code = random.randint(1000, 9999)
    email_subject = 'Password Reset Code'
    email_body = 'Hi user,' + '\n Welcome to Can-Dect! \n Please use the below Code to change your password. \n Code: {} '.format(
        code)
    data = {'email_body': email_body,
            'email': data['email'], 'subject': email_subject}
    Util.send_email(data)
    return Response(code)


@api_view(['PUT'])
def Verification(request, pk):
    userPass = UserDetail.objects.get(email=pk)
    userPass.is_Verified = True
    userPass.save()
    return Response('verified')


@api_view(['POST'])
def Create_User(request):
    data = request.data
    try:
        userSign = UserDetail.objects.create_user(
            email=data['email'],
            password=data['password'],
        )
        seralizer = UserSignUpSerial(userSign, many=False)
        return Response('Successful')

    except django.db.utils.IntegrityError:
        userSigndetails = UserDetail.objects.get(email=data['email'])
        serializer1 = UserSignUpSerial(userSigndetails, many=False)
        if serializer1.data != '':
            return Response('Email exists')
    except:

        return Response('Invalid Email')


@api_view(['POST'])
def UserDataEntry(request):
    if request.method == 'POST':
        data = request.data
        try:
            email = data['useremail_id']
            FirstName = data['firstname']
            LastName = data['lastname']
            age = data['age']
            phone = data['phone']
            gender = data['gender']
            address = data['address']
            UserData(useremail_id=email, FirstName=FirstName, LastName=LastName, age=age, phone=phone, gender=gender,
                     address=address).save()
            userPass = UserDetail.objects.get(id=email)
            userPass.has_data = True
            userPass.save()
            return Response('Successful')
        except django.db.utils.IntegrityError:
            return Response('not Successful')


# {
#     "useremail_id": 1,
#     "firstname": "prince",
#     "lastname": "paniyar",
#     "age": 22,
#     "phone": 9854022447,
#     "gender": "Male",
#     "address": "anamnagar"
# }


@api_view(['GET'])
def SignupData(request, emaildata):
    userSigndetails = UserDetail.objects.get(email=emaildata)
    serializer = UserSignUpDataSerial(userSigndetails, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def usersData(request, emaildata):
    userdetails = UserData.objects.get(useremail=emaildata)
    serializer = UserdetaSerial(userdetails, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def usersReportData(request):
    userdetails = UserData.objects.all()
    serializer = UserReportSerial(userdetails, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def updateUserPassword(request, pk):
    data = request.data
    oldpw = data['old']
    newpw = data['new']
    user = authenticate(username=pk, password=oldpw)
    if user is not None:
        userPass = UserDetail.objects.get(email=pk)
        userPass.set_password(newpw)
        userPass.save()
        return Response('Password Updated')
    else:
        return Response('error')


@api_view(['POST'])
def forgetUserPassword(request, pk):
    data = request.data
    newpw = data['password']
    userPass = UserDetail.objects.get(email=pk)
    userPass.set_password(newpw)
    userPass.save()
    return Response('Password Updated')


@api_view(['POST'])
def updateUserdetail(request, pk):
    data = request.data
    age = data['age']
    address = data['address']
    phone = data['phone']
    userPass = UserData.objects.get(useremail=pk)
    userPass.age = age
    userPass.address = address
    userPass.phone = phone
    userPass.save()
    return Response('Updated')


@api_view(['POST'])
def Login_User(request):
    global email, password
    if request.method == 'POST':
        data = request.data
        email = data['email']
        password = data['password']
        # print(email)
        # print(password)
    try:
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            userdetails = UserDetail.objects.get(email=email)
            serializer = UserhasDataSerial(userdetails, many=False)
            return Response(serializer.data)
        else:
            return Response('invalid')
    except UserDetail.DoesNotExist:
        return Response('not present')


@api_view(['POST'])
def LogOut_User(request):
    logout(request)
    return Response('Logged Out')


# Admin panel

def adminLogin(request):
    if request.method == 'POST':
        form = AdminLog(request.POST)
        if form.is_valid():
            useremail = form.cleaned_data['Useremail']
            password = form.cleaned_data['Password']
            user = authenticate(username=useremail, password=password)
            if user is not None:
                if user.admin:
                    login(request, user)
                    messages.error(request, 'Successfully Logged In')
                    return HttpResponseRedirect('/home')
                else:
                    messages.error(request, 'Credentials does not match')
            else:
                messages.error(request, 'username Password not matched')
    form = AdminLog()
    return render(request, '../templates/loginPage.html', {'form': form})
