import base64

from rest_framework import serializers
from report import models


class ReportSerial(serializers.ModelSerializer):
    ReportPDF = serializers.SerializerMethodField("get_image")
    class Meta:
        model = models.ReportDetail
        fields = ['id','Patient','Disease','Status','AdditionalDetails','Date','ReportPDF']

    def get_image(request, image: models.ReportDetail):
        with open(image.ReportPDF.name, 'rb') as loadedfile:
            return base64.b64encode(loadedfile.read())