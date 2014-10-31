from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
	lista_post = Post.objects.all().order_by('-fecha_creacion')[:5]
	contex = {'lista_pos': lista_post}
	return render(request, 'blog/index.html', contex)


def detalle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detalle.html', {'post': post})


