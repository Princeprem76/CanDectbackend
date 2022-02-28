from django.urls import path

from payment.views import paymentDetail, displayDetail,viewPaymentData

urlpatterns = [
    path('paymentsuccess/', paymentDetail),
    path('paymentdata/<int:pk>/', displayDetail),
    
]
