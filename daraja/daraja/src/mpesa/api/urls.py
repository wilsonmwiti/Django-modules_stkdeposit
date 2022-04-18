"""daraja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include


from .views import LNMCallbackUrlAPIView,C2BValidationAPIView,C2BConfirmationAPIView


urlpatterns = [
  
    path('lnm/', LNMCallbackUrlAPIView.as_view(),name="lnm-callbackurl"),
    path('c2b-validation/', C2BValidationAPIView.as_view(),name="c2b-validation"),
    path('c2b-confirmation/',C2BConfirmationAPIView.as_view(),name="c2b-confirmation"),

   

]

