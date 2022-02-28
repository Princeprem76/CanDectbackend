from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from services.forms import createService
from .models import AddService
from .serializers import ServicesSerial


# Create your views here.

@api_view(['POST'])
def CreateService(request):
    data = request.data
    form = AddService.objects.create(
        services=data['services'],
        price=data['price']
    )
    formserializer = ServicesSerial(form, many=False)
    if formserializer.is_valid():
        formserializer.save()
        return Response("Submitted!")


@api_view(['GET'])
def ServiceData(request):
    services = AddService.objects.all()
    serializer = ServicesSerial(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ServiceDataname(request, serviceid):
    services = AddService.objects.get(id=serviceid)
    serializer = ServicesSerial(services, many=False)
    return Response(serializer.data)


# Admin
@login_required
def AdminService(request):
    if request.method == 'POST':
        form = createService(request.POST)
        if form.is_valid():
            form.save()
            servicedat = AddService.objects.all()
            context = {
                'form': form
            }
            return render(request, '../templates/services.html',
                          {'form': form, 'serv': servicedat, 'homelink': 'http://127.0.0.1:8000/home',
                           'bookinglink': 'http://127.0.0.1:8000/booking',
                           'paymentlink': 'http://127.0.0.1:8000/payment',
                           'servicelink': 'http://127.0.0.1:8000/service',
                           'doctorlink': 'http://127.0.0.1:8000/signupdoctor'})
        else:

            return HttpResponse('Error')

    form = createService()
    servicedat = AddService.objects.all()
    return render(request, '../templates/services.html',
                  {'form': form, 'serv': servicedat, 'homelink': 'http://127.0.0.1:8000/home',
                   'bookinglink': 'http://127.0.0.1:8000/booking', 'paymentlink': 'http://127.0.0.1:8000/payment',
                   'servicelink': 'http://127.0.0.1:8000/service', 'doctorlink': 'http://127.0.0.1:8000/signupdoctor'})


@login_required
def deleteserv(request, id):
    if request.method == 'POST':
        dat = AddService.objects.get(pk=id)
        dat.delete()
        return HttpResponseRedirect('/service')


@login_required
def editService(request, id):
    if request.method == 'POST':
        data = AddService.objects.get(pk=id)
        servicesform = createService(request.POST, instance=data)
        if servicesform.is_valid():
            servicesform.save()
            return HttpResponseRedirect('/service')
    else:
        data = AddService.objects.get(pk=id)
        servicesform = createService(instance=data)

    return render(request, '../templates/editservice.html', {'form': servicesform, 'homelink': '/home', 'bookinglink': '/booking', 'paymentlink': '/payment',
                   'servicelink': '/service', 'doctorlink': '/signupdoctor'})
