from django.conf.urls import url

from polls import views
from polls.models import *
from django.views.generic import *


urlpatterns = [
    url(r'^accueil$', views.index, name='index'),
     url(r'^Article_Humor$', views.articleHumor.as_view()),
]