from django.contrib import admin
from django.urls import path
from paginas.views import frase_motivacional

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frase/', frase_motivacional, name='frase_do_dia'),
]