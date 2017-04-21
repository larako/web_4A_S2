from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(widget=forms.Textarea)
	def search(self):

		pass

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm", widget=forms.PasswordInput)
    email = forms.CharField(label="Email", widget=forms.EmailInput)
