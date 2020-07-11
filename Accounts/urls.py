from django.contrib import admin
from django.urls import path, include
from Accounts.views import company_signup


urlpatterns = [
    path ('accounts/signup/company/', company_signup, name='signup-company') 
]