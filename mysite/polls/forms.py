from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(widget=forms.Textarea)
	def search(self):

		pass