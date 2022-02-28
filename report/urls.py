from django.urls import path
from .views import ReportValid, reportData

urlpatterns = [
    path('report/', ReportValid),
    path('viewReport/<int:userID>/', reportData)
]
