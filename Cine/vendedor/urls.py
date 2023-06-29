from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cartelera/', views.cartelera, name='cartelera'),
    path('boleteria/', views.boleteria, name='boleteria'),
    path('about/', views.about, name='about'),
    path('boleteria/compra_exitosa', views.compra_exitosa, name='compra_exitosa')
]
