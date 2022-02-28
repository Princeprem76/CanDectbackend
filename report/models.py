from django.db import models
from userSignup.models import UserData


# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance, filename)


class ReportDetail(models.Model):
    stat = [('Positive', 'Positive'), ('Negative', 'Negative'), ('Normal', 'Normal'), ('High', 'High'), ('Low', 'Low')]
    Patient = models.ForeignKey(UserData, on_delete=models.CASCADE)
    Disease = models.CharField(max_length=120)
    Status = models.CharField(max_length=120, choices=stat)
    AdditionalDetails = models.TextField('Additional Details')
    Date = models.DateField(auto_now=True)
    ReportPDF = models.FileField('Report PDF', blank=True, upload_to=user_directory_path)
