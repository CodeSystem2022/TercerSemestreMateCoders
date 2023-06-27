from django.shortcuts import render, redirect
from .models import Pelicula, Sala, Funcion
from .forms import CompraForm
from django.contrib.auth.hashers import make_password
from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    # Verificar si el inicio de sesión fue exitoso
    login_success = request.session.pop('login_success', False)
    return render(request, 'home.html', {'user': request.user, 'login_success': login_success})

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
            total = precio_mayores * entradas_mayores + precio_menores * entradas_menores
            form.total = total
            form.save()
            
            butacas_ocupadas = Funcion.objects.get(id=funcion).asientos_ocupados
            return render(request, 'seleccionar_butacas.html', {'form': form, 'butacas_ocupadas': butacas_ocupadas})
    else:
        form = CompraForm()
    
    butacas_ocupadas = Funcion.objects.get(id=2).asientos_ocupados
    return render(request, 'boleteria.html', {'form': form})

def about(request):
    return render(request, 'about.html', {})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.contraseña = make_password(form.cleaned_data['contraseña'])
            usuario.save()
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '¡Inicio de sesión exitoso!')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return redirect('home')

