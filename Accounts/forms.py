from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from .models import CompanyUser


class CompanySignupForm(SignupForm):
    # declare here all the extra fields in CompanyUser model WITHOUT
    # the OneToOneField to User
    # (N.B: do NOT try to declare Meta class with model=CompanyUser,
    # it won't work!)
    company_name = forms.CharField(max_length=50, required=True, strip=True)

    # Override the save method to save the extra fields
    # (otherwise the form will save the User instance only)
    def save(self, request):
        # Save the User instance and get a reference to it
        user = super(CompanySignupForm, self).save(request)
        # Create an instance of your model with the extra fields
        # then save it.
        # (N.B: the are already cleaned, but if you want to do some
        # extra cleaning just override the clean method as usual)
        company_user = CompanyUser(
            contact_person=user,
            company_name=self.cleaned_data.get('company_name')
        )
        company_user.save()

        # Remember to return the User instance (not your custom user,
        # the Django one), otherwise you will get an error when the
        # complete_signup method will try to look at it.
        return company_user.contact_person