from .models import ProfileUser, ArtisantUser
from .forms import ProfileSignupForm, ArtisantSignupForm, UserProfileUpdateForm, UserUpdate, UserArtisantUpdateForm
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class ProfileUserSignupView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'Accounts/signup_user.html'
    
    # the previously created form class
    form_class = ProfileSignupForm

    # the view is created just a few lines below
    # N.B: use the same name or it will blow up
    view_name = 'signup_user'

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'


# Create the view (we will reference to it in the url patterns)
signup_user = ProfileUserSignupView.as_view()


class ArtisantUserSignupView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'Accounts/artisant_user.html'
    
    # the previously created form class
    form_class = ArtisantSignupForm

    # the view is created just a few lines below
    # N.B: use the same name or it will blow up
    view_name = 'artisant_user'

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'


# Create the view (we will reference to it in the url patterns)
artisant_user = ArtisantUserSignupView.as_view()


class PortfoliosUpdateView(UpdateView):
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


class UserUpdateView(UpdateView):
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


class ArtisantUpdateView(UpdateView):
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

def profil(request):
    return render(request, 'Accounts/Profile.html')
