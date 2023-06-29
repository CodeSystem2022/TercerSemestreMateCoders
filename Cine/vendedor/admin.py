from django.contrib import admin
from .models import Funcion, Sala, Precio, Pelicula, Compra

@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    pass

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    pass

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    pass

@admin.register(Precio)
class PrecioAdmin(admin.ModelAdmin):
    pass

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    pass