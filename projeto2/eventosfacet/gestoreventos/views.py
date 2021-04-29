from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Curso
from .forms import CursoForm

# Create your views here.
def index(request):
    return render(request, 'gestoreventos/index.html')

@login_required
def cursos(request):
    cursos = Curso.objects.filter(owner=request.user).order_by('id')
    context = {'cursos': cursos}
    return render(request, 'gestoreventos/cursos.html', context)

@login_required
def novo_curso(request):
    # Verificar se a página é requisitada pelo método POST
    # Pesquisem os métodos GET e POST
    if request.method != 'POST':
        form = CursoForm
    else:
        form = CursoForm(request.POST)
        if form.is_valid():
            novo_curso = form.save(commit=False)
            novo_curso.owner = request.user
            novo_curso.save()
            return HttpResponseRedirect(reverse('gestoreventos:cursos'))
    context = {'form': form}
    return render(request, 'gestoreventos/novo_curso.html', context)

@login_required
def edit_curso(request, edit_id):
    curso = Curso.objects.get(id=edit_id)
    if curso.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = CursoForm(instance=curso)
    else:
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gestoreventos:cursos'))
    
    context = {'curso': curso, 'form' : form}
    return render(request, 'gestoreventos/edit_curso.html', context)