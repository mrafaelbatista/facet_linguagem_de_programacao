from django.shortcuts import render
from .models import Assunto

# Create your views here.

def index(request):
    return render(request, 'ouvidoria/index.html')

def topicos(request):
    topicos = Topico.objects.order_by('id')
    context = {'abacate': topicos}
    return render(request, 'ouvidoria/topicos.html', context)
