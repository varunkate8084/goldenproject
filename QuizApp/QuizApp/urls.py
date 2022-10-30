"""QuizApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import RegistrationController
from .import UserLogInController
from . import AdminLogInController
urlpatterns = [
    path('admin/', admin.site.urls),
    # Registration Controller Urls
    path('registrationform/',RegistrationController.Action_Registration),
    path('submitdetails',RegistrationController.Submit_Record),
    path('showuserdetails/',RegistrationController.DisplayAllRecords),
    path('startquiz/',RegistrationController.Action_StartQuiz),

    # UserLogIn Controller Urls
    path('userlogin/',UserLogInController.Action_LogIn),
    path('checkuser',UserLogInController.UserLogIn_Check),
    # path('userlogout/',UserLogInController.User_LogOut),
    path('scoreboard/',UserLogInController.Action_ScoreBoard),

    #AdminLogIn Controller Urls
    path('adminlogin/',AdminLogInController.Action_LogIn),
    path('checkadmin',AdminLogInController.AdminLogIn_Check),
    path('adminlogout/',AdminLogInController.Admin_LogOut),
]
