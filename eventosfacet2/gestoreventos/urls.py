from django.urls import path
from . import views

app_name = 'gestoreventos'

urlpatterns = [
    
    # Página inicial
    path('', views.index, name='index'),
]
