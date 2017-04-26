from django.conf.urls import url
from django.contrib.auth import views as auth_views
from polls import views
from polls.models import *
from django.views.generic import *

urlpatterns = [
    url(r'^accueil$', views.index.as_view(), name='index'),
    url(r'^Search$', views.Search.as_view(), name='Search'),
    url(r'^Spectacles_Humor$', views.spectaclesHumor.as_view()),
    url(r'^Spectacles_Theater$', views.spectaclesTheater.as_view()),
    url(r'^Spectacles_Danse$', views.spectaclesDanse.as_view()),
    url(r'^Festivals_Rock$', views.festivalsRocks.as_view()),
    url(r'^Festivals_Electro$', views.festivalsElectro.as_view()),
    url(r'^Festivals_HipHop$', views.festivalsHipHop.as_view()),

    url(r'^ExpoGrandPalais$', views.expoGrandPalais.as_view()),
    url(r'^Expo_Museum$', views.expoMuseum.as_view()),
    url(r'^Expo_Expo$', views.expoExpo.as_view()),
    url(r'^Concerts_Rock$', views.concertsRock.as_view()),
    url(r'^Concerts_Electro$', views.concertsElectro.as_view()),
    url(r'^Concerts_HipHop$', views.concertsHipHop.as_view()),

    url(r'^Spectacles_Humor/(?P<pk>\d+)$', views.article.as_view(), name='spectacles_humor'),
    url(r'^Spectacles_Theater/(?P<pk>\d+)$', views.article.as_view(), name='spectacles_theater'),
    url(r'^Spectacles_Danse/(?P<pk>\d+)$', views.article.as_view(), name='spectacles_danse'),
    url(r'^Festivals_Rock/(?P<pk>\d+)$', views.article.as_view(), name='festival_rocks'),
    url(r'^Festivals_Electro/(?P<pk>\d+)$', views.article.as_view(), name='festival_electro'),
    url(r'^Festivals_HipHop/(?P<pk>\d+)$', views.article.as_view(), name='festival_hip-hop'),

    url(r'^ExpoGrandPalais/(?P<pk>\d+)$', views.article.as_view(), name='expo_grand-palais'),
    url(r'^Expo_Museum/(?P<pk>\d+)$', views.article.as_view(), name='expo_museum'),
    url(r'^Expo_Expo/(?P<pk>\d+)$', views.article.as_view(), name='expo_expo'),
    url(r'^Concerts_Rock/(?P<pk>\d+)$', views.article.as_view(), name='concert_rock'),
    url(r'^Concerts_Electro/(?P<pk>\d+)$', views.article.as_view(), name='concert_electro'),
    url(r'^Concerts_HipHop/(?P<pk>\d+)$', views.article.as_view(), name='concert_hip-hop'),
    
    url(r'^signin/*$', views.connexion, name='connexion'),
    url(r'^signout/*$', views.deconnexion, name='deconnexion'),
    url(r'^signup/*$', views.signup, name='signup'),
    url(r'^profile$', views.userUpdate, name='userUpdate'),
    url(r'^cpassword/$', views.change_password, name='change_password'),

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^paypal/create-payment/$', views.create_payment, name='create_payment'),

]
