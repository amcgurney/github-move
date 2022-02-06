from django.shortcuts import render
from django.views.generic.base import TemplateView # <- View class to handle requests
from .models import Artist

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["duke"] = Artist.objects.all()
        return context