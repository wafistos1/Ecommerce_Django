from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class PrivateUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class CompanyUser(models.Model):
    contact_person = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"{self.contact_person.username}-[{self.company_name}]"