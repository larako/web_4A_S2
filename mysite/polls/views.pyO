from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.template import loader
from polls.models import *
import operator
from django.db.models import Q
from functools import reduce

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


class Search (ListView):
	model = Spectacles
	context_object_name = "article"
	template_name= 'polls/articles.html'
	def get_queryset(self):
		result = super(Search, self).get_queryset()
		query = self.request.GET.get('q')
		if query:
			query_list = query.split()
			result = result.filter(
				reduce(operator.and_,
					(Q(name__icontains=q) for q in query_list))|
				reduce(operator.and_,
					(Q(artistes__name__icontains=q) for q in query_list))

			)
		return result
# Create your views here.
