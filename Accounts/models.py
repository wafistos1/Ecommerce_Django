from django.db import models
from django.contrib.auth.models import User 

Peintre = 'Peintre'
Menuisier = 'Menuisier'
Plombier = 'Plombier'
Carreleur = 'Carreleur'
TYPE_CHOICES = [
    (Peintre, 'Peintre'),
    (Menuisier, 'Menuisier'),
    (Plombier, 'Plombier'),
    (Carreleur, 'Carreleur'),
]
# Create your models here.
class ArtisantUser(models.Model):

    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=244, choices=TYPE_CHOICES, default=Peintre)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username}-[{self.profession}]"


class CompanyUser(models.Model):
    contact_person = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"{self.contact_person.username}-[{self.company_name}]"