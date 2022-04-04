from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ReportForm
from .models import ReportDetail
from .serializers import ReportSerial
from rest_framework.decorators import api_view
from rest_framework.response import Response

fs = FileSystemStorage(location='reports/')


# Create your views here.
@api_view(['POST'])
def ReportValid(request):
    if request.method == 'POST':
        data = request.data
        try:
            csv_file = data['file']
            if not csv_file.name.endswith('.pdf'):
                return Response('Error')
            content = csv_file.read()
            file_content = ContentFile(content)
            file_name = fs.save(
                "_report_{}_{}.pdf".format(data['patient_id'], data['diseases']), file_content
            )
            tmp_file = fs.path(file_name)
            Patient = int(data['patient_id'])
            status = data['status']
            Disease = data['diseases']
            AdditionalDetails = data['adddetails']
            ReportPDF = tmp_file

            ReportDetail(Status=status, Patient_id=Patient, Disease=Disease, AdditionalDetails=AdditionalDetails,
                         ReportPDF=ReportPDF).save()

            return Response('Successful')
        except:
            return Response('not successful')


@api_view(['GET'])
def reportData(request, userID):
    reports = ReportDetail.objects.filter(Patient_id=userID)
    serializer = ReportSerial(reports, many=True)
    return Response(serializer.data)
