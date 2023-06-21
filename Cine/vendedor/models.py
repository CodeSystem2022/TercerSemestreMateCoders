from django.db import models

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
    
    def __str__(self):
        return self.title
    
class Sala(models.Model):
    name = models.CharField(
        max_length=20,
        blank=False, 
        null=False,
        choices=(
            ('Sala 1'),
            ('Sala 2'),
            ('Sala 3')
        ))
    
    def __str__(self):
        return self.name

class Funcion(models.Model):
    pelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE)
    sala = models.ForeignKey('Sala', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    precio_mayores = models.DecimalField(max_digits=8, decimal_places=2)
    precio_menores = models.DecimalField(max_digits=8, decimal_places=2)
    asientos_ocupados = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.pelicula} - {self.sala} - {self.fecha} {self.hora}' 

class Entrada(models.Model):
    funcion = models.ForeignKey('Funcion', on_delete=models.CASCADE)
    numero_asiento = models.CharField(max_length=10),
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    
