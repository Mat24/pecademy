from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


# Create your models here.

"""

class usuario(models.Model):
   # pais = ((u'colomnia', u'ecuador', u'panama', u'mexico', u'costarica', u'Test', u'Otros'),(u'blog', u'Blog'),)
    nombre =   models.CharField(max_length=50)
    apellido =  models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    usuario  = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    #pais = models.CharField(max_length=50, choices=pais, default='colombia')
    ciudad = models.CharField(max_length=50)
    telefono = models.IntegerField()
    #imagem

"""


class Publica(models.Model):
    usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    departamento = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    #imagen
    #sitio = models.URLField()


class Post(models.Model):
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	fecha_creacion = models.DateTimeField()
    #fecha modificacion
    #visitas
	autor = models.ForeignKey(Publica)
    #imagen
    #tags
    #usuario
    #categoria
    #comentario
    #categoria

	def __str__(self):
		return self.titulo

"""
class Comentario(models.Model):
    post = models.ForeignKey(Post)
    usuario = models.ForeignKey(usuario) #contendra el id del usuario junto a el nombre de usuario
    contenido = models.TextField()
    fecha = models.DateTimeField() #fecha en la que se publico el comentario

    """