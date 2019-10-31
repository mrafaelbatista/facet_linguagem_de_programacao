from django.urls import path
from . import views

urlpatterns = [
    #A view abaixo ainda não existe
    path('', views.index, name='index')
]