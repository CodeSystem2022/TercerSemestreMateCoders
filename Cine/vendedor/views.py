from django.shortcuts import render
from .models import Pelicula, Sala

def home(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'home.html', {'peliculas': peliculas})

def cartelera(request):
    
    return render(request, 'cartelera.html', {})

def boleteria(request):
    return render(request, 'boleteria.html', {})

def about(request):
    return render(request, 'about.html', {})