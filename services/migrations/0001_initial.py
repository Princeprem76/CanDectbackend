# Generated by Django 3.2.8 on 2021-11-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.CharField(max_length=200)),
                ('price', models.PositiveSmallIntegerField()),
            ],
        ),
    ]