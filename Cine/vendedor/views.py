from django.shortcuts import render
from .models import Pelicula, Sala, Funcion

def home(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'home.html', {'peliculas': peliculas})

def cartelera(request):
    
    return render(request, 'cartelera.html', {})

def boleteria(request):
    butacas_ocupadas = Funcion.objects.get(id=2).asientos_ocupados
    return render(request, 'boleteria.html', {'butacas_ocupadas': butacas_ocupadas})

def about(request):
    return render(request, 'about.html', {})