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
import requests
import json
from requests.auth import HTTPBasicAuth
from django.http import JsonResponse

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

class spectaclesDanse(ListView):
    model = Spectacles
    template_name= 'polls/articles.html'
    queryset = Spectacles.objects.filter(categories__name__exact='Spectacles_Danse')
    def get_context_data(self, **kwargs):
        ctx= super(spectaclesDanse,self).get_context_data(**kwargs)
        ctx['title']="Danse Spectacles"
        return ctx

class spectaclesTheater(ListView):
    model = Spectacles
    template_name= 'polls/articles.html'
    queryset = Spectacles.objects.filter(categories__name__exact='Spectacles_Theater')
    def get_context_data(self, **kwargs):
        ctx= super(spectaclesTheater,self).get_context_data(**kwargs)
        ctx['title']="Spectacles Theater"
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
        return redirect("/")
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

@login_required
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

@login_required
def create_payment(request):

    url = 'https://api.sandbox.paypal.com/v1/oauth2/token'
    headers = {"Accept":"application/json", "Accept-Language":"en_US"}
    username = "AY4_ODDSaxYXQuHlGctxmcuVJupD0Q1Nj8qPzG7TE6n99FXKrZeuWmFN9T8PMH0K2eRhCdBkAz0f7Fkh"
    password = "EM1s7qcrVsotqkXK0-HRCjLaywRUujyDCORgc2vZNotQGK_iUmt8jC2ihjy2zZ7YicdjxTvP2C_LRbZZ"
    r = requests.post(url, headers=headers, auth=(username, password), data={'grant_type':'client_credentials'})

    response = json.loads(r.text)
    token = response['access_token']

    url = 'https://api.sandbox.paypal.com/v1/payments/payment'
    headers = {"Content-Type":"application/json", "Authorization":"Bearer " + token}
    payload = {"intent":"sale",
              "redirect_urls":{
                "return_url":"http://example.com/your_redirect_url.html",
                "cancel_url":"http://example.com/your_cancel_url.html"
              },
              "payer":{
                "payment_method":"paypal"
              },
              "transactions":[
                {
                  "amount":{
                    "total":"7.47",
                    "currency":"EUR"
                  }
                }
              ]
              }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    response = json.loads(r.text)
    trans_id = response['id']
    trans_state = response['state']

    return JsonResponse({'paymentID':trans_id})
    #data = {}
    #data['paymentID'] = trans_id
    #json_data = json.dumps(data)
    #print(json_data)
    #return render(request, 'polls/create_payment.html')
# Create your views here.
