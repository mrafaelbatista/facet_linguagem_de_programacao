from django.shortcuts import render
from .models import Topico

# Create your views here.
def index(request):
    return render(request, 'ouvidoria/index.html')

def topicos(request):
    topicos = Topico.objects.order_by('id')
    context = {'topicos': topicos}
    return render(request, 'ouvidoria/topicos.html', context)
