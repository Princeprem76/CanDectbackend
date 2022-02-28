from django.urls import path
from .views import Create_User, Login_User, SignupData, usersData, UserDataEntry, send_code, usersReportData, \
    Verification, LogOut_User, updateUserdetail, updateUserPassword, send_password_code, forgetUserPassword,adminLogin

urlpatterns = [
    path('Signup/', Create_User),
    path('viewSignupDetail/<str:emaildata>/', SignupData),
    path('detail/', UserDataEntry),
    path('viewUserdetail/<int:emaildata>/', usersData),
    path('viewuserReport/', usersReportData),
    path('verify/', send_code),
    path('verifypassword/', send_password_code),
    path('getverify/<str:pk>/', Verification),
    path('userlogin/', Login_User),
    path('userlogout/', LogOut_User),
    path('updateUserdetail/<int:pk>/', updateUserdetail),
    path('updateUserpw/<str:pk>/', updateUserPassword),
    path('fogetUserpw/<str:pk>/', forgetUserPassword),
    
]
