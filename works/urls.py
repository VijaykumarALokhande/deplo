from django.urls import path
from . import views

#from django.views.static import serve
#from django.conf.urls import urls


urlpatterns = [
    path('', views.home, name='workspagename'),
]
