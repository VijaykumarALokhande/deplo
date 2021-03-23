
from django.contrib import admin
from django.urls import path
from . import views

#from django.views.static import serve
#from django.conf.urls import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fn),
    #url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
