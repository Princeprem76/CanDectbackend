# Generated by Django 3.2.8 on 2021-11-22 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50, verbose_name='First Name')),
                ('LastName', models.CharField(max_length=50, verbose_name='Last Name')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Age')),
                ('phone', models.PositiveBigIntegerField(unique=True, verbose_name='Phone Number')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Female', max_length=20, verbose_name='Gender')),
                ('address', models.CharField(max_length=80, verbose_name='Address')),
                ('useremail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userSignup.userdetail')),
            ],
        ),
    ]
