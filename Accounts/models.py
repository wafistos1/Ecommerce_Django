from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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


class ImagesArtisant(models.Model):
    Artisant_images = models.ForeignKey(ArtisantUser, on_delete=models.CASCADE, related_name='user_image')
    image = models.ImageField(upload_to='picture/artisant/images/', null=True)

    class Meta:
        ordering = ('Artisant_images',)

    def __str__(self):
        return self.Artisant_images.user.username
    
    def get_absolute_url(self):
        pass
    
    def get_update_url(self): 
        pass