
from django.contrib import admin
from django.urls import path
#from . import views
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
#from django.views.static import serve
#from django.conf.urls import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='homepagename'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
