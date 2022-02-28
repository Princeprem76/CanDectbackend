from django.shortcuts import render
from .forms import NotifyForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NotifySerial,NotifyUserSerial
from .models import notifyDetail


# Create your views here.
@api_view(['POST'])
def CreateNotify(request):
    if request.method == 'POST':
        data = request.data
        try:
            Doctor_Name = data['doctor_id']
            Patient_Name = data['patient_id']
            message = data['message']
            notifyDetail(Doctor_Name_id=Doctor_Name, Patient_Name_id=Patient_Name, Mesage=message).save()
            return Response('Successful')
        except:
            return Response('error')


@api_view(['GET'])
def NotifyData(request, userID):
    notific = notifyDetail.objects.filter(Patient_Name_id=userID)
    serializer = NotifyUserSerial(notific, many=True)
    return Response(serializer.data)
