from django.urls import path
from . import views

app_name = 'ouvidoria'

urlpatterns = [
    #Página inicial
    path('', views.index, name='index'),
]