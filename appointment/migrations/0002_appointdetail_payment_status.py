# Generated by Django 3.2.8 on 2022-02-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointdetail',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]