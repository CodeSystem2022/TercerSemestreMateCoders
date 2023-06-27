from django.db import models
from django.utils import timezone
import json

def sala_vacia():
    with open('sala.JSON', 'r') as file:
        return json.load(file)

class Pelicula(models.Model):
    title = models.CharField(max_length=70, blank=False, null=False)
    age_classification = models.CharField(
        max_length=3,
        blank=False,
        null=False,
        choices=(
            ('ATP', 'Apta para Todo Publico'),
            ('+13', 'Sólo apta para mayores de 13 años'),
            ('+16', 'Sólo apta para mayores de 16 años'),
            ('+18', 'Sólo apta para mayores de 18 años'),
            ('C', 'Sólo apta para mayores de 18 años exhibición condicionada')
        ))
    idioma = models.CharField(max_length=20, blank=False, null=False, default='Es', choices=(('Es', 'Español'), ('En', 'Ingles'), ('Pr', 'Portugues')))
    subtitulos = models.BooleanField(default=False)
    cartel = models.ImageField(upload_to='images/', default='static/images/no-image.png')
    director = models.CharField(max_length=50, blank=False, null=False, default="--")
    publicadora = models.CharField(max_length=50, blank=False, null=False, default="--")
    fecha_estreno = models.DateField(blank=False, null=False, default=timezone.now)
    
    
    def __str__(self):
        return self.title
    
class Sala(models.Model):
    name = models.CharField(
        max_length=20,
        blank=False, 
        null=False,
        choices=(
            ('1', 'Sala 1'),
            ('2', 'Sala 2'),
            ('3', 'Sala 3')
        ))
    
    def __str__(self):
        return self.name

class Precio(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    mayores = models.DecimalField(max_digits=8, decimal_places=2)
    menores = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name} - Menores: {self.menores}  Mayores: {self.mayores}'
    

class Funcion(models.Model):
    pelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE)
    sala = models.ForeignKey('Sala', on_delete=models.CASCADE)
    precio = models.ForeignKey('Precio', on_delete=models.CASCADE)
    fecha = models.DateField(blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)
    asientos_ocupados = models.JSONField(default=sala_vacia)

    def __str__(self):
        return f'{self.pelicula} - {self.sala} - {self.fecha} {self.hora}' 

class Compra(models.Model):
    funcion = models.ForeignKey('Funcion', on_delete=models.CASCADE)
    entradas_menores = models.IntegerField(blank=False, null=False)
    entradas_mayores = models.IntegerField(blank=False, null=False)
    asientos = models.JSONField(default=dict)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return f'Asientos: {self.asientos} - Total: {self.total} Función: {self.funcion}'
    
