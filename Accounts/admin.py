from django.contrib import admin
from .models import CompanyUser, PrivateUser

# Register your models here.
admin.site.register(CompanyUser)
admin.site.register(PrivateUser) 