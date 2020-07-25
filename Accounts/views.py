from .models import ProfileUser, ArtisantUser, ImagesArtisant
from .forms import ProfileSignupForm, ArtisantSignupForm, UserProfileUpdateForm, UserUpdate, UserArtisantUpdateForm, ImageForm
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


class ProfileUserSignupView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'Accounts/signup_user.html'
    
    # the previously created form class
    form_class = ProfileSignupForm
    view_name = 'signup_user'


# Create the view (we will reference to it in the url patterns)
signup_user = ProfileUserSignupView.as_view()


class ArtisantUserSignupView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'Accounts/artisant_user.html'
    form_class = ArtisantSignupForm
    view_name = 'artisant_user'


# Create the view (we will reference to it in the url patterns)
artisant_user = ArtisantUserSignupView.as_view()


class PortfoliosUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileUpdateForm
    model = ProfileUser
    template_name = 'Accounts/profile_update.html'
    success_url = 'profil'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        #save cleaned post data
        clean = form.cleaned_data
        self.object = form.save()
        return super(PortfoliosUpdateView, self).form_valid(form)
   

PortfoliosUpdate = PortfoliosUpdateView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdate
    model = User
    template_name = 'Accounts/user_update.html'
    success_url = 'profil'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        #save cleaned post data
        clean = form.cleaned_data
        self.object = form.save()
        return super(UserUpdateView, self).form_valid(form)
   

UserUpdateView = UserUpdateView.as_view()


class ArtisantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserArtisantUpdateForm
    model = ProfileUser
    template_name = 'Accounts/artisant_update.html'
    success_url = 'profil'

    def get_object(self, queryset=None):
        return self.request.user.artisant

    def form_valid(self, form):
        #save cleaned post data
        clean = form.cleaned_data
        self.object = form.save()
        return super(ArtisantUpdateView, self).form_valid(form)
   

ArtisantUpdate = ArtisantUpdateView.as_view()

@login_required(login_url='account_login')
def profil(request):
    artisant = None
    profile = None
    try:
        artisant = ArtisantUser.objects.get(user=request.user.id)
        print(artisant)
        print('Success artisant')
    except:
        pass        
    try:
        profile = ProfileUser.objects.get(profile_user=request.user.id)
        print(profile)
        print('Success profile')
    except:
        pass

    context = {
        'artisant': artisant,
        'profile': profile,
    }
    return render(request, 'Accounts/Profile.html', context)


@login_required(login_url='account_login')
def AddArtisantImages(request):
    print(request.user.id)
    ImageFormSet = modelformset_factory(ImagesArtisant, form=ImageForm, extra=1, max_num=4, validate_max=True)
    artisant = get_object_or_404(ArtisantUser, user=request.user.id)
    # print(artisant)
    
    
    if request.method == 'POST':
        formset = ImageFormSet(
            request.POST,
            request.FILES,
            queryset=ImagesArtisant.objects.none()
            )
        if formset.is_valid():
            for form in formset:
                data = form.cleaned_data
                image = data.get('image')
                photo = ImagesArtisant(Artisant_images=artisant, image=image)
                photo.save()
            return redirect('profil')
        else:
            print(formset.errors)
            print(f'formset is not valid')
    else:
        formset = ImageFormSet(queryset=ImagesArtisant.objects.none())
    formset = ImageFormSet(queryset=ImagesArtisant.objects.none())
    context = {
        'formset': formset,
    }
    return render(request, 'Accounts/images.html', context)


@login_required(login_url='account_login')
def artisant_job(request):
    artisant = None
    try:
        artisant = ArtisantUser.objects.get(user=request.user.id)
        print(artisant)
        print('Success artisant')
    except:
        pass

    context = {
        'artisant': artisant,
    }
    return render(request, 'Accounts/artisant_job.html', context)