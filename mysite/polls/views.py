from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.template import loader
from polls.models import *

class index(ListView):
	model = Spectacles
	template_name= 'polls/index.html'

class spectaclesHumor(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Spectacles_Humor')


class spectaclesTheater(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Spectacles_Theater')

class spectaclesDanse(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Spectacles_Danse')

class festivalsRocks(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Festival_Rocks')

class festivalsElectro(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Festival_Electro')

class festivalsHipHop(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Festival_HIP-HOP')




class concertsRock(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Concert_Rock')

class concertsElectro(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Concert_Electro')

class concertsHipHop(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Concert_HIP-HOP')

class expoGrandPalais(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Expo_Grand Palais')

class expoMuseum(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Expo_Museum')

class expoExpo(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Expo_Expo')


class article(DetailView):
	model = Spectacles
	context_object_name = "article"
	template_name= 'polls/article.html'
# Create your views here.
