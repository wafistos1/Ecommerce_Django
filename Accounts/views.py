from .models import ProfileUser, ArtisantUser
from .forms import ProfileSignupForm, ArtisantSignupForm
from allauth.account.views import SignupView 


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
