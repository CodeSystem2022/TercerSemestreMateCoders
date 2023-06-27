from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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
    total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Asientos: {self.asientos} - Total: {self.total} Función: {self.funcion}'
    



class UsuarioManager(BaseUserManager):
    def create_user(self, correo, contraseña=None, **extra_fields):
        if not correo:
            raise ValueError('El correo electrónico debe ser proporcionado')
        correo = self.normalize_email(correo)
        usuario = self.model(correo=correo, **extra_fields)
        usuario.set_password(contraseña)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, contraseña=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(correo, contraseña, **extra_fields)

class Usuario(AbstractBaseUser):
    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'

    def __str__(self):
        return self.correo

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
