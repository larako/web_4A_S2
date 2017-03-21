from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('polls/index.html')
    return render(request, 'polls/index.html',None)

def article(request):
    template = loader.get_template('polls/article.html')
    return render(request, 'polls/article.html',None)
# Create your views here.
