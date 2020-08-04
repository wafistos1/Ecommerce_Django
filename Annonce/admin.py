from django.contrib import admin

# Register your models here.
from .models import Annonce, Comment, ImageAnnonce, Categories

# Register your models here.
admin.site.register(ImageAnnonce)  # delete group
admin.site.register(Annonce)  # delete group
admin.site.register(Comment)  # delete group
admin.site.register(Categories)   # delete group