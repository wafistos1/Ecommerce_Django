from django import forms
from .models import Annonce, ImageAnnonce

class AnnonceFrom(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = '__all__'
        exclude = ['owner']


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = ImageAnnonce
        fields = ('image', )