# Generated by Django 3.2.8 on 2021-11-22 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctorSignup', '0001_initial'),
        ('userSignup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notifyDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now=True)),
                ('Mesage', models.TextField()),
                ('Doctor_Name', models.ForeignKey(max_length=120, on_delete=django.db.models.deletion.CASCADE, to='doctorSignup.doctordetail')),
                ('Patient_Name', models.ForeignKey(max_length=120, on_delete=django.db.models.deletion.CASCADE, to='userSignup.userdata')),
            ],
        ),
    ]