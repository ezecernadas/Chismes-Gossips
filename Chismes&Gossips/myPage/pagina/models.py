from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
class Agenda(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    
class Usuarios(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
   
class Publicaciones(models.Model):
    idUsuario=models.IntegerField()
    contenido= models.CharField(max_length=500)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    dislike = models.IntegerField()
    
    
