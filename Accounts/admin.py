from django.contrib import admin
from .models import ProfileUser, ArtisantUser, ImagesArtisant

# Register your models here.
admin.site.register(ProfileUser)
admin.site.register(ImagesArtisant)
admin.site.register(ArtisantUser)