from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.template import loader
from polls.models import *

def index(request):
    template = loader.get_template('polls/index.html')
    return render(request, 'polls/index.html',None)

class articleHumor(ListView):
	model = Spectacles
	template_name= 'polls/articleHumor.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Spectacles_Humor')
# Create your views here.
