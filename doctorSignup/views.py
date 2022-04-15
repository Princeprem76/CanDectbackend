import re

import pandas as pd
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from sklearn.preprocessing import StandardScaler
from tensorflow import keras

from userSignup.models import UserDetail, UserData
from .forms import CreateDoctorForm, DoctorEmailForm

from .models import DoctorsData

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DoctorSignUpSerial, DoctorDataSerial, DoctorIDSerial, DoctorupdatedetailSerial

fs = FileSystemStorage(location='tmp/')
model = keras.models.load_model('cancerDet.h5')
ecgmodel = keras.models.load_model('ecgDet.h5')


@api_view(['GET'])
def DoctorData(request, doctoremail):
    doctors = DoctorsData.objects.get(Doctoremail__email=doctoremail)
    serializer = DoctorupdatedetailSerial(doctors, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def DoctorDatas(request, doctoremail):
    doctors = DoctorsData.objects.get(Doctoremail__email=doctoremail)
    serializer = DoctorDataSerial(doctors, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def AppointmentDoctor(request, serviceid):
    doctorData = DoctorsData.objects.filter(field=serviceid)
    serializer = DoctorDataSerial(doctorData, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def Login_Doctor(request):
    global email, password
    if request.method == 'POST':
        data = request.data
        email = data['email']
        password = data['password']
    try:
        user = authenticate(username=email, password=password)
        if user is not None:
            doctorData = UserDetail.objects.get(email=email)
            if doctorData.is_staff == True:
                login(request, user)
                doctorData = DoctorsData.objects.get(Doctoremail__email=email)
                serializer = DoctorIDSerial(doctorData, many=False)
                return Response(serializer.data)
            else:
                return Response("Notdoctor")
        else:
            return Response("not successful")
    except:
        return Response('no data')


@api_view(['PUT'])
def updateDoctordetail(request, doctoremail):
    data = request.data
    age = data['age']
    address = data['address']
    phone = data['phone']
    userPass = DoctorsData.objects.get(Doctoremail__email=doctoremail)
    serializer = DoctorupdatedetailSerial(
        userPass, age=age, address=address, phone=phone)
    serializer.save()
    return Response('Updated')


@login_required(login_url='/adminLogin')
def LogOut(request):
    logout(request)
    messages.error(request, 'Successfully Logged out!')
    return HttpResponseRedirect('/adminLogin')


# Admin
@login_required(login_url='/adminLogin')
def doctorEmailA(request):
    if request.method == 'POST':
        form = DoctorEmailForm(request.POST or None)
        if form.is_valid():
            useremail = form.cleaned_data['Useremail']
            password = form.cleaned_data['Password']
            user = UserDetail.objects.create_doctoruser(
                email=useremail, password=password)
            user.save()
            form = DoctorEmailForm()
            messages.error(request, 'Doctor Credentials Added')
            return HttpResponseRedirect('/addDoctor')
        else:
            form = DoctorEmailForm()

    form = DoctorEmailForm()
    return render(request, '../templates/doctorsign.html', {'form': form, 'homelink': '/home',
                                                            'bookinglink': '/booking',
                                                            'paymentlink': '/payment',
                                                            'servicelink': '/service',
                                                            'doctorlink': '/signupdoctor'})


@api_view(['POST'])
def detection(request):
    if request.method == 'POST':
        doc = request.FILES  # returns a dict-like object
        csv_file = doc['file']
        if not csv_file.name.endswith('.csv'):
            return Response('Error')
        content = csv_file.read()
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)
        reader = pd.read_csv(tmp_file)
        value = [[]]
        for idd, row in enumerate(reader):
            value[0].append(row)
        scaler = StandardScaler()
        x_train = scaler.fit_transform(value)
        x_train = x_train.reshape(len(x_train), x_train.shape[1], -1)
        his = model.predict(x_train)
        if his[0] == 0:
            his = 'Normal'
        else:
            his = 'Melignent'
        return Response(his)


@api_view(['POST'])
def ecgdetection(request):
    if request.method == 'POST':
        doc = request.FILES  # returns a dict-like object
        csv_file = doc['file']
        if not csv_file.name.endswith('.csv'):
            return Response('Error')
        content = csv_file.read()
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)
        reader = pd.read_csv(tmp_file)
        value = [[]]
        for idd, row in enumerate(reader):
            dat = re.sub(r'^([^.]*\.[^.]*)\.', r'\1', str(row))
            value[0].append(float(dat))
        scaler = StandardScaler()
        x_train = scaler.fit_transform(value)
        x_train = x_train.reshape(len(x_train), x_train.shape[1], -1)
        his = ecgmodel.predict(x_train)
        b = 0
        temps = his
        for iter_num in range(len(his[0]) - 1, 0, -1):
            for idx in range(iter_num):
                if his[0][idx] > his[0][idx + 1]:
                    temp = his[0][idx]
                    his[0][idx] = his[0][idx + 1]
                    his[0][idx + 1] = temp

        for iter_num in range(len(temps[0]) - 1, 0, -1):
            for i in range(iter_num):
                print(temps[0][i])
                print(his[0][4])
                if temps[0][i] == his[0][4]:
                    b = i
        if b == 0:
            return Response('Normal')
        elif b == 1:
            return Response('Unknown')
        elif b == 2:
            return Response('Ventricular ectopic')
        elif b == 3:
            return Response('Supraventricular ectopic')
        else:
            return Response('Fusion Beat')


@login_required(login_url='/adminLogin')
def doctorAdd(request):
    if request.method == 'POST':
        form = CreateDoctorForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.error(request, 'Doctor Details Added')
            return HttpResponseRedirect('/signupdoctor')

        else:
            form = CreateDoctorForm()

    form = CreateDoctorForm()
    return render(request, '../templates/Doctor.html',
                  {'form': form, 'homelink': '/home', 'bookinglink': '/booking', 'paymentlink': '/payment',
                   'servicelink': '/service', 'doctorlink': '/signupdoctor'})


@login_required(login_url='/adminLogin')
def doctDat(request):
    dat = DoctorsData.objects.all()
    doctdat = DoctorsData.objects.all().count()
    userdat = UserData.objects.all().count()
    users = UserData.objects.all()
    return render(request, '../templates/homepage.html',
                  {'doct': dat, 'users': users, 'userform': userdat, 'doctorform': doctdat, 'homelink': '/home',
                   'bookinglink': '/booking', 'paymentlink': '/payment', 'servicelink': '/service',
                   'doctorlink': '/signupdoctor'})


@login_required(login_url='/adminLogin')
def deleteDat(request, id):
    if request.method == 'POST':
        dat = UserDetail.objects.get(email=id)
        dat.delete()
        messages.error(request, 'Doctor data has been deleted')
        return HttpResponseRedirect('/home')


@login_required(login_url='/adminLogin')
def editDoctor(request, id):
    if request.method == 'POST':
        data = DoctorsData.objects.get(pk=id)
        doctorform = CreateDoctorForm(request.POST, instance=data)
        if doctorform.is_valid():
            doctorform.save()
            messages.error(request, 'Doctor data updated')
            return HttpResponseRedirect('/home')
    else:
        data = DoctorsData.objects.get(pk=id)
        doctorform = CreateDoctorForm(instance=data)

    return render(request, '../templates/edit.html',
                  {'form': doctorform, 'homelink': '/home', 'bookinglink': '/booking', 'paymentlink': '/payment',
                   'servicelink': '/service', 'doctorlink': '/signupdoctor'})
