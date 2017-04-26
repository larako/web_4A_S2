from django import forms
from django.utils.translation import ugettext_lazy as _


class CheckoutForm(forms.Form):
	payment_method_nonce = forms.CharField(label="Payment_method_nonce", max_length=1000, widget=forms.widgets.HiddenInput)
    
	def clean(self):
		self.cleaned_data = super(CheckoutForm, self).clean()
		# Braintree nonce is missing
		if not self.cleaned_data.get('payment_method_nonce'):
				raise forms.ValidationError(_(		
			'We couldn\'t verify your payment. Please try again.'))
		return self.cleaned_data



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
