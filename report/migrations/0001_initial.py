# Generated by Django 3.2.8 on 2021-11-22 09:38

from django.db import migrations, models
import django.db.models.deletion
import report.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userSignup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Disease', models.CharField(max_length=120)),
                ('Status', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative'), ('Normal', 'Normal'), ('High', 'High'), ('Low', 'Low')], max_length=120)),
                ('AdditionalDetails', models.TextField(verbose_name='Additional Details')),
                ('Date', models.DateField(auto_now=True)),
                ('ReportPDF', models.FileField(blank=True, upload_to=report.models.user_directory_path, verbose_name='Report PDF')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userSignup.userdata')),
            ],
        ),
    ]
