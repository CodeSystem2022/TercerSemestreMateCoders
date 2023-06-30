from django.shortcuts import render
from .models import Pelicula, Sala, Funcion, Compra
from .forms import CompraForm
from decimal import Decimal
import json
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
            cantidad_entradas = int(entradas_mayores) + int(entradas_menores)
            form.total = total
        
            instancia = form.save()
            id_compra = instancia.id
            butacas_ocupadas = Funcion.objects.get(id=funcion).asientos_ocupados
            return render(request, 'seleccionar_butacas.html', {'id_compra': id_compra, 'butacas_ocupadas': butacas_ocupadas, 'cantidad_entradas': cantidad_entradas})
    else:
        form = CompraForm()
    
    butacas_ocupadas = Funcion.objects.get(id=2).asientos_ocupados
    return render(request, 'boleteria.html', {'form': form})

def about(request):
    return render(request, 'about.html', {})

def compra_exitosa(request):
    if request.method == 'POST':
        datos_compra = request.POST.items()
        entradas = [tupla for tupla in datos_compra if isinstance(tupla[0],str) and "butaca" in tupla[0]]
        butacas = {tupla[0].split('_')[1]: bool(tupla[1].lower()) for tupla in entradas}
        data = json.dumps(butacas)
        id_compra = request.POST.get("compra_id")
        compra = Compra.objects.get(id = id_compra)
        compra.asientos = data
        funcion = Funcion.objects.get(id=compra.funcion.id)
        asientos_funcion = funcion.asientos_ocupados
        for butaca, valor in butacas.items():
            asientos_funcion[butaca]=valor
        data = json.dumps(asientos_funcion)
        funcion.asientos_ocupados = asientos_funcion
        funcion.save()
        compra.save()


    

        return render(request, 'ticket.html', {'compra':compra})
    

