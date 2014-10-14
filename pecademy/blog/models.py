from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Post(models.Model):
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	fecha_creacion = models.DateTimeField()


	def __str__(self):
		return self.titulo
