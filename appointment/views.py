import datetime

import django.db
from django.contrib.auth.decorators import login_required
from django.db.models import query as q
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dateutil.parser import parse
from .models import AppointDetail
from .serializers import appointUserSerial, appointDoctorSerial


# Create your views here.
@api_view(['POST'])
def CreateAppoint(request):
    data = request.data
    try:
        purpose_id = data['purpose_id']
        Doctor_id = data['doctor_id']
        patient_id = data['user_id']
        date = data['date']
        times = parse(data['time'])
        price = data['price']
        AppointDetail(purpose_id=purpose_id, Doctor_id=Doctor_id, patient_id=patient_id, date=date, times=times,
                      price=price).save()
        return Response("Successful")
    except django.db.utils.IntegrityError:
        return Response("error")


@api_view(['GET'])
def AppointData(request, userID):
    appoint = AppointDetail.objects.filter(patient_id=userID)
    serializer = appointUserSerial(appoint, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AppointdoctorData(request, userID):
    appoint = AppointDetail.objects.filter(Doctor_id=userID)
    serializer = appointDoctorSerial(appoint, many=True)
    return Response(serializer.data)

# Admin


@login_required
def Bookingdet(request):
    now = datetime.datetime.now()
    booki = AppointDetail.objects.filter(date=datetime.date.today())

    return render(request, '../templates/bookingDetail.html', {'form': booki, 'homelink': 'http://127.0.0.1:8000/home', 'bookinglink': 'http://127.0.0.1:8000/booking', 'paymentlink': 'http://127.0.0.1:8000/payment', 'servicelink': 'http://127.0.0.1:8000/service', 'doctorlink': 'http://127.0.0.1:8000/signupdoctor'})
