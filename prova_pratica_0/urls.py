from django.urls import path
from prova_pratica_0.views import *

app_name="prova_pratica_0"
urlpatterns=[
    path('index', index, name='index'),
    path('somma', somma, name='somma'),
    path('media', media, name='media')
]