from django.urls import path

from .views import NotifyData, CreateNotify

urlpatterns = [
    path('notify/', CreateNotify),
    path('viewNotify/<int:userID>/', NotifyData)
]
