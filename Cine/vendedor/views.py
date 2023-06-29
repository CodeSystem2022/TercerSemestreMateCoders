from django.shortcuts import render
from .models import Pelicula, Sala, Funcion
from .forms import CompraForm
from decimal import Decimal
from django.http import HttpResponse

def home(request):
    ultimas_peliculas = Pelicula.objects.order_by('-fecha_estreno')[:5]
    return render(request, 'home.html', {'peliculas': ultimas_peliculas})

def cartelera(request):
    funciones = Funcion.objects.all()
    return render(request, 'cartelera.html', {'funciones': funciones})

def boleteria(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            funcion = request.POST.get('funcion')
            precio_mayores = Funcion.objects.get(id=funcion).precio.mayores
            precio_menores = Funcion.objects.get(id=funcion).precio.menores
            entradas_mayores = request.POST.get('entradas_mayores')
            entradas_menores = request.POST.get('entradas_menores')
            total = precio_mayores * Decimal(entradas_mayores) + precio_menores * Decimal(entradas_menores)
            cantidad_entradas = entradas_mayores + entradas_menores
            form.total = total
        
            form.save()
            
            butacas_ocupadas = Funcion.objects.get(id=funcion).asientos_ocupados
            return render(request, 'seleccionar_butacas.html', {'form': form, 'butacas_ocupadas': butacas_ocupadas, 'cantidad_entradas': cantidad_entradas})
    else:
        form = CompraForm()
    
    butacas_ocupadas = Funcion.objects.get(id=2).asientos_ocupados
    return render(request, 'boleteria.html', {'form': form})

def about(request):
    return render(request, 'about.html', {})

def compra_exitosa(request):
    if request.method == 'POST':
        butacas = request.POST.items()
        return HttpResponse(butacas)

