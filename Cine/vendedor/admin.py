from django.contrib import admin
from .models import Funcion, Sala, Precio, Pelicula, Compra

@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ['pelicula', 'sala', 'fecha', 'hora',]
    date_hierarchy = 'fecha'
    

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ['name',]
    

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['title', 'age_classification', 'idioma', 'fecha_estreno',  ]
    date_hierarchy = 'fecha_estreno'
    list_filter = ['age_classification',]
    

@admin.register(Precio)
class PrecioAdmin(admin.ModelAdmin):
    list_display = ['name', 'menores', 'mayores',]
    

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['funcion', 'entradas_menores', 'entradas_mayores', ]
    