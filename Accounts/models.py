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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="artisant")
    profession = models.CharField(max_length=244, choices=TYPE_CHOICES, default=Peintre)
    description = models.TextField()
    is_artisant = models.BooleanField()
    avatar = models.ImageField(default='default_artisant.jpg', upload_to='picture/artisant/', null=True)

    def __str__(self):
        return f"{self.user.username}-[{self.profession}]"


class ProfileUser(models.Model):
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    picture = models.ImageField(default='default.jpg', upload_to='picture/')

    def __str__(self):
        return f"{self.profile_user.username}"