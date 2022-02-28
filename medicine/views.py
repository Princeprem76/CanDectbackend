from django.shortcuts import render
from .forms import MedicineForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MedicineSerial
from .models import medicineDetail


# Create your views here.
@api_view(['POST'])
def Create_Medicine(request):
    if request.method == 'POST':
        data = request.data
        try:
            Doctor_Name = data['doctor_id']
            Patient_Name = data['patient_id']
            Disease = data['diseases']
            Medicine = data['medicine']
            medicineDetail(Doctor_Name_id=Doctor_Name, Patient_Name_id=Patient_Name, Disease=Disease,
                           Medicine=Medicine).save()
            return Response('Successful')
        except:
            return Response('error')


@api_view(['GET'])
def MedicineData(request, userID):
    medicines = medicineDetail.objects.filter(Patient_Name_id=userID)
    serializer = MedicineSerial(medicines, many=True)
    return Response(serializer.data)
