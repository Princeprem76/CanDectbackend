from django.shortcuts import render
from .forms import ReportForm
from .models import ReportDetail
from .serializers import ReportSerial
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['POST'])
def ReportValid(request):
    if request.method == 'POST':
        data = request.data
        try:
            Patient = data['patient_id']
            status = data['status']
            Disease = data['diseases']
            AdditionalDetails = data['adddetails']
            ReportPDF = data['pdf']
            ReportDetail(status=status, Patient_id=Patient, Disease=Disease, AdditionalDetails=AdditionalDetails,
                         ReportPDF=ReportPDF).save()
            return Response('Successful')
        except:
            return Response('not successful')


@api_view(['GET'])
def reportData(request, userID):
    reports = ReportDetail.objects.filter(Patient_id=userID)
    serializer = ReportSerial(reports, many=True)
    return Response(serializer.data)
