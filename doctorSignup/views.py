import pandas as pd
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
    doctors = DoctorsData.objects.get(Doctoremail=doctoremail)
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
            login(request, user)
            doctorData = UserDetail.objects.get(email=email)
            serializer = DoctorIDSerial(doctorData, many=False)
            return Response(serializer.data)
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
    userPass = DoctorData.objects.get(email=doctoremail)
    serializer = DoctorupdatedetailSerial(
        userPass, age=age, address=address, phone=phone)
    serializer.save()
    return Response('Updated')


@login_required
def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/adminLogin')


# Admin
@login_required
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
            return HttpResponseRedirect('/addDoctor')
        else:
            form = DoctorEmailForm()

    form = DoctorEmailForm()
    return render(request, '../templates/doctorsign.html', {'form': form, 'homelink': 'http://127.0.0.1:8000/home',
                                                            'bookinglink': 'http://127.0.0.1:8000/booking',
                                                            'paymentlink': 'http://127.0.0.1:8000/payment',
                                                            'servicelink': 'http://127.0.0.1:8000/service',
                                                            'doctorlink': 'http://127.0.0.1:8000/signupdoctor'})


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
            print(row)
            value[0].append(float(row))
        scaler = StandardScaler()
        x_train = scaler.fit_transform(value)
        x_train = x_train.reshape(len(x_train), x_train.shape[1], -1)
        his = ecgmodel.predict(x_train)
        if his[0] == 0:
            his = 'Normal'
        else:
            his = 'Melignent'
        return Response(his)


@login_required
def doctorAdd(request):
    if request.method == 'POST':
        form = CreateDoctorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/signupdoctor')

        else:
            form = CreateDoctorForm()

    form = CreateDoctorForm()
    return render(request, '../templates/Doctor.html',
                  {'form': form, 'homelink': '/home', 'bookinglink': '/booking', 'paymentlink': '/payment',
                   'servicelink': '/service', 'doctorlink': '/signupdoctor'})


@login_required
def doctDat(request):
    dat = DoctorsData.objects.all()
    doctdat = DoctorsData.objects.all().count()
    userdat = UserData.objects.all().count()
    users = UserData.objects.all()
    return render(request, '../templates/homepage.html',
                  {'doct': dat, 'users': users, 'userform': userdat, 'doctorform': doctdat, 'homelink': '/home',
                   'bookinglink': '/booking', 'paymentlink': '/payment', 'servicelink': '/service',
                   'doctorlink': '/signupdoctor'})


@login_required
def deleteDat(request, id):
    if request.method == 'POST':
        dat = UserDetail.objects.get(email=id)
        dat.delete()
        return HttpResponseRedirect('/home')


@login_required
def editDoctor(request, id):
    if request.method == 'POST':
        data = DoctorsData.objects.get(pk=id)
        doctorform = CreateDoctorForm(request.POST, instance=data)
        if doctorform.is_valid():
            doctorform.save()
            return HttpResponseRedirect('/home')
    else:
        data = DoctorsData.objects.get(pk=id)
        doctorform = CreateDoctorForm(instance=data)

    return render(request, '../templates/edit.html',
                  {'form': doctorform, 'homelink': '/home', 'bookinglink': '/booking', 'paymentlink': '/payment',
                   'servicelink': '/service', 'doctorlink': '/signupdoctor'})
