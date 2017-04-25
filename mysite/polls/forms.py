from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.Textarea)
    def search(self):

        pass

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SignupForm(forms.Form):
    fname = forms.CharField(label="First Name", max_length=30)
    lname = forms.CharField(label="Last Name", max_length=30)
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm", widget=forms.PasswordInput)
    email = forms.CharField(label="Email", widget=forms.EmailInput)

#class UpdateProfile(forms.Form):
#   email = forms.CharField(label="Email", widget=forms.EmailInput)

class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

#class UserAccountForm(forms.Form):
#    firstname = forms.CharField(label="First namegecd my   ", max_length=30)
#    lastname = forms.CharField(label="Last name", max_length=30)
#    confirm_password = forms.CharField(label="Confirm", widget=forms.PasswordInput)
#    email = forms.CharField(label="Email", widget=forms.EmailInput)
