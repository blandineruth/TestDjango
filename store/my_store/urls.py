from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),  # Associer la vue nav à l'URL vide pour la page d'accueil
    path("/about", views.about, name="about"),
    path("/furniture", views.furniture, name="furniture"),
    path("/blog", views.blog, name="blog"),
    path("/contact", views.contact, name="contact"),
    

]


