from django.db import models

# Create your models here.


class Blog(models.Model):
	
	#detalles de blog 
	autor = models.CharField(max_length=200)
	fecha_creacion = models.DateTimeField('fecha creacion')
	fecha_actualizacion = models.DateTimeField('fecha actulizacion')
	fecha_publicacion = models.DateTimeField('fecha publicacion')
	contenido = models.TextField()
	titulo = models.CharField(max_length=200)
	estado = models.IntegerField(default=0, blank=True, editable=False)
	con_vistas = models.IntegerField(default=0, blank=True, editable=False)
	etiqueas = models.CharField(max_length=200)
	imagen = models.ImageField(upload_to='templates/static/media/upload/blog')

	#comentarios
	comentario = models.CharField(max_length=200)
	estado_comentario = models.IntegerField(default=0, blank=True, editable=False)
	con_comentarios = models.IntegerField(default=0, blank=True, editable=False)
	usuario = models.CharField(max_length=200)
	fecha_publicacion = models.DateTimeField('fecha de publicacion de comentario')

    
