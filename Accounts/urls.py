
from django.urls import path, include
from Accounts.views import signup_user, artisant_user


urlpatterns = [
    path('accounts/signup/user/', signup_user, name='signup_user'),
    path('accounts/signup/artisant_user/', artisant_user, name='artisant_user'),
]