from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^accueil$', views.index, name='index'),
     url(r'^article$', views.article, name='article'),
]