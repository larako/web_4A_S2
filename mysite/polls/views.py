from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import *
from django.template import loader
from polls.models import *
import operator
from django.db.models import Q
from functools import reduce
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
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


def connexion(request):
    error = False
    next = ""
    if request.GET:  
        next = request.GET['next']
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                if next == "":
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    return HttpResponseRedirect(next)
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'polls/connexion.html', locals())

def deconnexion(request):
    logout(request)
    next = ""
    if request.GET:  
        next = request.GET['next']
    if next == "":
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(next)

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
            fname = form.cleaned_data["fname"]
            lname = form.cleaned_data["lname"]
            if password != confirm_password:
                errorpasswd = True
            else:
                if re.fullmatch("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])([a-zA-Z0-9]{8,})$", password) is not None:
                    user, created = User.objects.get_or_create(username=username, email=email)
                    if created:  # Utilisateur crée
                        user.set_password(password)
                        user.first_name = fname
                        user.last_name = lname
                        user.save() #enregistre l'utilisateur
                    else: 
                        error = True
                else:
                    errorpasswd2 = True
    else:
        form = SignupForm()
    return render(request, 'polls/signup.html', locals())

@login_required
def userUpdate(request):
    if request.method == 'POST':
        form = UserUpdate(data=request.POST, instance=request.user)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
    else:
            form = UserUpdate(instance=request.user)

    return render(request, 'polls/profile.html', locals())

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'polls/change_password.html', {
        'form': form
    })
# Create your views here.
