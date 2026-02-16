from django.urls import path
from .views import view_a, view_b, view_c, view_d
app_name = "voti"
urlpatterns = [
    path("listematerie", view_a, name="listematerie"),
    path("maxMinVoti", view_b, name="maxMinVoti"),
    path("mediastudenti", view_c, name="mediastudenti"),
    path("votistudenti", view_d, name="votistudenti")
]