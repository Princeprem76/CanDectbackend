import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from payment.models import payments
from payment.serializers import paymentSerial, paymentDisplaySerial


@api_view(['POST'])
def paymentDetail(request):
    if request.method == "POST":
        data = request.data
        try:
            price = data['price']
            payment_method = data['payment_method']
            user = data['user']
            service = data['service']
            payment_done = data['pay']
            payments(price=price, payment_method=payment_method, user_id=user, service_id=service,
                     payment_done=payment_done).save()
            return Response('Success')
        except:
            return Response('Error')


# #
# {
# "price": 1000,
# "payment_method": "Cash",
# "user": 10,
# "service": 1,
# "pay": "False"
# }


@api_view(['GET'])
def displayDetail(request, pk):
    displaydata = payments.objects.filter(user_id=pk)
    serializer = paymentDisplaySerial(displaydata, many=True)
    return Response(serializer.data)


# Admin
@login_required
def viewPaymentData(request):
    dat = payments.objects.all().order_by('-id')
    return render(request, '../templates/payment.html', {'form': dat, 'homelink': 'http://127.0.0.1:8000/home',
                                                         'bookinglink': 'http://127.0.0.1:8000/booking',
                                                         'paymentlink': 'http://127.0.0.1:8000/payment',
                                                         'servicelink': 'http://127.0.0.1:8000/service',
                                                         'doctorlink': 'http://127.0.0.1:8000/signupdoctor'})
