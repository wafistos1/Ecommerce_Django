from django.db import models
import uuid
from django.urls import reverse
from Accounts.models import ArtisantUser, ImagesArtisant, ProfileUser

class Categories(models.Model):
    Plomberie = 'Plomberie'
    Peinture = 'Peinture'
    Menuiserie = 'Menuiserie'
    Service = 'Service'
    Autres = 'Autres'
    TYPE_CHOICES = [
        (Plomberie, 'Plomberie'),
        (Peinture, 'Peinture'),
        (Menuiserie, 'Menuiserie'),
        (Service, 'Service'),
        (Autres, 'Autres'),
    ]
    type_job = models.CharField(max_length=100, choices=TYPE_CHOICES, default=Service )\
    
    def __str__(self):
        return self.type_job
class Annonce(models.Model):
    """
    class for Product user
    """
    Started = 'started'
    Deal = 'Deal'
    Finished = 'Finished' 
    Closed = 'Closed'
    Canceled = 'Canceled'
    list_status = [
        (Started, 'Started'), 
        (Deal, 'Deal'), 
        (Finished, 'Finished'), 
        (Closed, 'Closed'),
        (Canceled, 'Canceled'),
    ]
    id = models.UUIDField(  
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    owner = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=list_status, default=Started)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    view_annonce = models.IntegerField(blank=True, null=True, default=0)
    favorite = models.ManyToManyField(ProfileUser, related_name='favorite', blank=True)

    class Meta:
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('annonce_detail', args=[str(self.id)])
    
    def get_favorite_url(self):  # new
        return reverse('favorite_annonce', args=[str(self.id)])
    
    def get_update_url(self):  # new
        return reverse('annonce_update', args=[str(self.id)])
    
    def get_delete_url(self):  # new
        return reverse('annonce_delete', args=[str(self.id)])
    

class ImageAnnonce(models.Model):
    annonce_images = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='image')
    image = models.FileField(upload_to='images/', default='image_default.jpg', blank=True, null=True)
    
    class Meta:
        pass

    def __str__(self):
        return self.annonce_images.title
    
    def get_absolute_url(self):
        return reverse("annonce_update_image", kwargs={"pk": self.pk})
    
    def get_update_url(self): 
        return reverse("annonce_image", kwargs={"pk": self.pk})


class Comment(models.Model):
    pass

class MpArtisan(models.Model):
    pass

class Like(models.Model):
    pass

class Rating(models.Model):
    pass