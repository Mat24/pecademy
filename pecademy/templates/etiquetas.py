	titulo = models.CharField("Nombre del evento", max_length=200)
	descripcion = models.CharField(null=True, blank=True, max_length=200)
	direccion = models.CharField(max_length=50)
	fecha_hora = models.DateTimeField()
	imagen = models.ImageField("Imágen", upload_to = 'templates/static/media/upload/eventos') #, default = 'templates/static/upload/no-img.jpg'
	posicion_geo = GeopositionField("Lugar")

	def filename(self):
		return os.path.basename(self.imagen.name)



	from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    categoria = ((u'noticias', u'Noticias'),(u'blog', u'Blog'),)

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creaccion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField(auto_now=True)
    categoria = models.CharField(max_length=50, choices=categoria, default='noticias')
    visitas = models.IntegerField(default=0, blank=True, editable=False)
    imagen = models.ImageField(upload_to='templates/static/media/upload/blog')
    autor = models.ForeignKey(User)
    email = models.EmailField()



    #slug

    def __unicode__(self):
        pos_titu_cate = "%s %s"%(self.titulo, self.categoria)
        return  pos_titu_cate



from django.shortcuts import render_to_response, get_object_or_404, redirect
from multimedia.models import Multimedia
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#categoria sera igual a musica o video, 
def post(request, slug):
	post = get_object_or_404(Multimedia, slug=slug)
	return render_to_response('detalle-musica.html',{'post':post})

def musica(request):
	return post_paginas(request, 'musica')

def videos(request):
	return post_paginas(request, 'video')

#https://docs.djangoproject.com/en/dev/topics/pagination/
def post_paginas(request, categoria):
	post_list = Multimedia.objects.filter(categoria=categoria).order_by('-id')
	paginator = Paginator(post_list, 8) # muestra 12 post por pagina
#    publicidad = Publicidad.objects.order_by()[:1]
 #   multimedia = Multimedia.objects.order_by().filter(categoria='musica')[:3]

	page = request.GET.get('page')
	try:
		posts=paginator.page(page)
	except PageNotAnInteger:
		# si la variable page no es un numero, que lo dewelva a la primera pagina
		posts=paginator.page(1)
	except EmptyPage:
		# si la variable page tiene un numero por ejemplo 9999, que lo envie a la ultima pagina
		posts=paginator.page(paginator.num_pages)

	return render_to_response(categoria+'.html',{'posts':posts})

