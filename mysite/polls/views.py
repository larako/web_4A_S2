from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import *
from django.template import loader
from polls.models import *
import operator
from django.db.models import Q
from functools import reduce
from django.contrib.auth import authenticate, login, logout
from polls.forms import *
from django.urls import reverse
from django.contrib.auth.models import User
import re 

class index(ListView):
	model = Spectacles
	template_name= 'polls/index.html'

class spectaclesHumor(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Spectacles_Humor')

	def get_context_data(self, **kwargs):
		ctx= super(spectaclesHumor,self).get_context_data(**kwargs)
		ctx['title']="Humor Spectacles"
		return ctx


class spectaclesTheater(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Spectacles_Theater')
	def get_context_data(self, **kwargs):
		ctx= super(spectaclesTheater,self).get_context_data(**kwargs)
		ctx['title']="Theater Spectacles"
		return ctx

class spectaclesDanse(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Spectacles_Danse')
	
	def get_context_data(self, **kwargs):
		ctx= super(spectaclesDanse,self).get_context_data(**kwargs)
		ctx['title']="Danse Spectacles"
		return ctx

class festivalsRocks(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Festival_Rocks')
	def get_context_data(self, **kwargs):
		ctx= super(festivalsRocks,self).get_context_data(**kwargs)
		ctx['title']="Rock Festivals"
		return ctx

class festivalsElectro(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Festival_Electro')
	def get_context_data(self, **kwargs):
		ctx= super(festivalsElectro,self).get_context_data(**kwargs)
		ctx['title']="Electro Festivals"
		return ctx

class festivalsHipHop(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Festival_HIP-HOP')
	def get_context_data(self, **kwargs):
		ctx= super(festivalsHipHop,self).get_context_data(**kwargs)
		ctx['title']="HipHop Festivals"
		return ctx



class concertsRock(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Concert_Rock')
	def get_context_data(self, **kwargs):
		ctx= super(concertsRock,self).get_context_data(**kwargs)
		ctx['title']="Rock Concerts"
		return ctx

class concertsElectro(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Concert_Electro')
	def get_context_data(self, **kwargs):
		ctx= super(concertsElectro,self).get_context_data(**kwargs)
		ctx['title']="Electro Concerts"
		return ctx

class concertsHipHop(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Concert_HIP-HOP')
	def get_context_data(self, **kwargs):
		ctx= super(concertsHipHop,self).get_context_data(**kwargs)
		ctx['title']="HipHop Concerts"
		return ctx

class expoGrandPalais(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Expo_Grand Palais')
	def get_context_data(self, **kwargs):
		ctx= super(expoGrandPalais,self).get_context_data(**kwargs)
		ctx['title']="Expo GrandPalais"
		return ctx

class expoMuseum(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Expo_Museum')
	def get_context_data(self, **kwargs):
		ctx= super(expoMuseum,self).get_context_data(**kwargs)
		ctx['title']="Expo Museum"
		return ctx

class expoExpo(ListView):
	model = Spectacles
	template_name= 'polls/articles.html'
	queryset = Spectacles.objects.filter(categories__name__exact='Expo_Expo')
	def get_context_data(self, **kwargs):
		ctx= super(expoExpo,self).get_context_data(**kwargs)
		ctx['title']="Expo EXpo"
		return ctx


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


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'polls/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect("/")

def signup(request):
    error = False
    errorpasswd = False

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            email = form.cleaned_data["email"]
            if password != confirm_password:
                errorpasswd = True
            else:
                if re.fullmatch("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])([a-zA-Z0-9]{8,})$", password) is not None:
                    user, created = User.objects.get_or_create(username=username, email=email)
                    if created:  # Utilisateur crée
                        user.set_password(password)
                        user.save() #enregistre l'utilisateur
                    else: 
                        error = True
                else:
                    errorpasswd2 = True
    else:
        form = SignupForm()
    return render(request, 'polls/signup.html', locals())
# Create your views here.
