from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pecademy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   	url(r'^$', 'home.views.index', name='index'),
   	url(r'^blog/', 'blog.views.index', name='index'),
   	url(r'^detalle/', 'blog.views.detalle', name='detalle'),
)
