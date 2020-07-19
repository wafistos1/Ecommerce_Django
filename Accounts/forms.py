from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from .models import ProfileUser, ArtisantUser, TYPE_CHOICES
from django.contrib.auth.forms import UserChangeForm  
from django.contrib.auth.models import User

class ProfileSignupForm(SignupForm):
    # declare here all the extra fields in CompanyUser model WITHOUT
    # the OneToOneField to User
    # (N.B: do NOT try to declare Meta class with model=CompanyUser,
    # it won't work!)
    picture = forms.ImageField()

    # Override the save method to save the extra fields
    # (otherwise the form will save the User instance only)
    def save(self, request):
        # Save the User instance and get a reference to it
        user = super(ProfileSignupForm, self).save(request)
        # Create an instance of your model with the extra fields
        # then save it.
        # (N.B: the are already cleaned, but if you want to do some
        # extra cleaning just override the clean method as usual)
        profile_user = ProfileUser(
            profile_user=user,
            picture=self.cleaned_data.get('picture')
        )
        profile_user.save()

        # Remember to return the User instance (not your custom user,
        # the Django one), otherwise you will get an error when the
        # complete_signup method will try to look at it.
        return profile_user.profile_user


class ArtisantSignupForm(SignupForm):
    # declare here all the extra fields in CompanyUser model WITHOUT
    # the OneToOneField to User
    # (N.B: do NOT try to declare Meta class with model=CompanyUser,
    # it won't work!)

    description = forms.CharField(max_length=50, required=True, strip=True, widget=forms.Textarea)
    profession = forms.CharField(max_length=200, widget=forms.Select(choices=TYPE_CHOICES)) 

    # Override the save method to save the extra fields
    # (otherwise the form will save the User instance only)
    def save(self, request):
        # Save the User instance and get a reference to it
        user = super(ArtisantSignupForm, self).save(request)
        # Create an instance of your model with the extra fields
        # then save it.
        # (N.B: the are already cleaned, but if you want to do some
        # extra cleaning just override the clean method as usual)
        artisant_user = ArtisantUser(
            user=user,
            profession=self.cleaned_data.get('profession'),
            description=self.cleaned_data.get('description'),
            is_artisant=True,
        )
        artisant_user.save()

        # Remember to return the User instance (not your custom user,
        # the Django one), otherwise you will get an error when the
        # complete_signup method will try to look at it.
        return artisant_user.user


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ('picture',)


class UserArtisantUpdateForm(forms.ModelForm):
    class Meta:
        model = ArtisantUser
        fields = ('profession', 'description', 'avatar', )


class UserUpdate(forms.ModelForm):
    class Meta:
        model = User 
        fields = ('username',) 