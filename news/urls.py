from django.urls import path
from .views import home, articoloDetailView, query, lista_articoli, giornalistaDetailView
app_name = "news"
urlpatterns = [
    path("", home, name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("query", query, name="query"),
    path("lista_articoli", lista_articoli, name="lista_articoli"),
    path("giornalista/<int:pk>", giornalistaDetailView, name="giornalista_detail")
]