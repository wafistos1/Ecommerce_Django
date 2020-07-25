from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR
from django.contrib.auth.decorators import login_required
from .forms import AnnonceFrom, ImageForm  #  editAnnonceForm, commentForm, MpUserForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Annonce, ArtisantUser, Comment, ImageAnnonce, Like
from Accounts.models import ArtisantUser, ProfileUser 


# Create your views here.
def home(request):
    """
    """
    return render(request, 'index.html')


@login_required(login_url='account_login')
def add_annonce(request):
    """
    Add annonces by users
    """
    ImageFormSet = modelformset_factory(ImageAnnonce, form=ImageForm, extra=4, max_num=4, validate_max=True)
    if request.method == "POST":
        a_form = AnnonceFrom(request.POST)
        formset = ImageFormSet(
            request.POST,
            request.FILES,
            queryset=ImageAnnonce.objects.none()
            )
        if a_form.is_valid() and formset.is_valid():
            user = request.user.profile
            annonceForm = a_form.save(commit=False)
            annonceForm.owner = user
            annonceForm.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = ImageAnnonce(annonce_images=annonceForm, image=image)
                    photo.save()
                    # capture_message(f"add annonce format valide utiliser par {request.user.username}", level="info")  
            messages.add_message(
                request, messages.SUCCESS, 'Annonce ajouter avec succès'
            )
            return redirect('home')
        else:
            print(a_form.errors)
            print('Is not valid')
            # capture_message(f"Annonce format non valide utiliser par {request.user.username}", level="error")   
    else:
        a_form = AnnonceFrom()
        formset = ImageFormSet(queryset=ImageAnnonce.objects.none())
    a_form = AnnonceFrom()
    formset = ImageFormSet(queryset=ImageAnnonce.objects.none())
    # capture_message(f"{request.user.username} try to update annonce", level="info")

    context = {
        "a_form": a_form,
        "formset": formset,
        }
    return render(request, 'Annonce/add.html', context)



