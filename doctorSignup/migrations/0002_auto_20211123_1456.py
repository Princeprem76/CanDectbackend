# Generated by Django 3.2.8 on 2021-11-23 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_alter_medicinedetail_doctor_name'),
        ('notification', '0002_alter_notifydetail_doctor_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctorSignup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorsdata',
            name='Doctoremail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='DoctorDetail',
        ),
    ]