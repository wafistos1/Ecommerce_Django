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
    annonces = Annonce.objects.all().order_by('-created')
    context = {
        'annonces': annonces
    }
    return render(request, 'Annonce/home.html', context)


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


def annonceDetailView(request, pk):
    """
        Class to display all annonces
    """
    details = Annonce.objects.get(pk=pk)
    details.view_annonce += 1
    details.save()

    # comment = Comment.objects.filter(
    #     for_post=details,
    #     reply=None).order_by('-create_content')
    # is_favorite = False
    # if details.favorite.filter(id=request.user.id).exists():
    #     is_favorite = True
    # else:
    #     print('favorite is now False')
    # if request.method == "POST":
    #     print(request.POST)
    #     c_form = commentForm(request.POST or None)
    #     if c_form.is_valid():
    #         content = request.POST.get('content')
    #         reply_id = request.POST.get('comment-id')
    #         comment_qs = None  # reply is null
    #         if reply_id:
    #             comment_qs = Comment.objects.get(id=reply_id)  
    #         comment_use = Comment(
    #             commented_by=request.user,
    #             for_post=details,
    #             content=content,
    #             reply=comment_qs
    #             )
    #         comment_use.save()
    # else:
    #     c_form = commentForm()
    # print(f'send {is_favorite}')
    context = {
        # 'is_favorite': is_favorite,
        'details': details,
        
        # 'comment': comment,
        # 'commentform': c_form,
        }
    # if request.is_ajax():
    #     print('Ajax is true')
    #     html = render_to_string(
    #         'annonce/comment.html',
    #         context, request=request
    #         )
    #     return JsonResponse({'form': html})
    return render(request, 'Annonce/detail.html', context)

@login_required(login_url='account_login')
def updateAnnonce(request, pk=None):
    """
    """
    ImageFormSet = modelformset_factory(ImageAnnonce, form=ImageForm, extra=4, max_num=4, validate_max=True)
    obj_annonce = get_object_or_404(Annonce, pk=pk)
    if request.method == "POST":
        form = AnnonceFrom(request.POST or None, instance=obj_annonce)
        formset = ImageFormSet(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            print('is valid')
            form.save()
            
            for form in formset.cleaned_data:
                try:
                    image = form['image']
                    photo = ImageAnnonce(annonce_images=obj_annonce, image=image)
                    photo.save()
                except:
                    print('Forme image non valide')                  
                    # capture_message(f"add annonce format valide utiliser par {request.user.username}", level="info")  
            messages.add_message(
                request, messages.SUCCESS, 'Annonce updated avec succès'
            )
            return redirect('home')
        else:
            print(form.errors)
            print('Is not valid')
            # capture_message(f"Annonce format non valide utiliser par {request.user.username}", level="error")   
    else:
        form = AnnonceFrom(instance=obj_annonce)
        formset = ImageFormSet(queryset=ImageAnnonce.objects.filter(annonce_images=obj_annonce))
    form = AnnonceFrom(instance=obj_annonce)
    formset = ImageFormSet(queryset=ImageAnnonce.objects.filter(annonce_images=obj_annonce))
    # capture_message(f"{request.user.username} try to update annonce", level="info")

    context = {
        'obj': obj_annonce,
        "a_form": form,
        "formset": formset,
        }
    return render(request, 'Annonce/update.html', context)


class AnnonceDeletelView(LoginRequiredMixin, DeleteView):
    """
    """
    model = Annonce
    context_object_name = 'obj_delete'
    template_name = 'Annonce/delete.html'
    success_url = reverse_lazy('home')