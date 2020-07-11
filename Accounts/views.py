from .models import CompanyUser, PrivateUser
from .forms import CompanySignupForm
from allauth.account.views import SignupView 

class CompanyUserSignupView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'Accounts/signup_user.html'
    # the previously created form class
    form_class = CompanySignupForm

    # the view is created just a few lines below
    # N.B: use the same name or it will blow up
    view_name = 'company_signup'

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'

# Create the view (we will reference to it in the url patterns)
company_signup = CompanyUserSignupView.as_view()