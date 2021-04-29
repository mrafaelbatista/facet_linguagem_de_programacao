# Views

from .models import Curso

def teste(request):
    cursos = Curso.objects.order_by('id')
    context = {'cursos': cursos}
    return render(request, 'gestoreventos/teste.html', context)


#teste.html - Testar a listagem de objetos
  <p>Cursos</p>

  <ul>
      {% for curso in cursos %}
          <li>{{ curso }}</li>
      {% empty %}
          <li>No topics have been added yet.</li>
      {% endfor %}
  </ul>

# Adicionar links para funções
<a href="{% url 'gestoreventos:index' %}">Página Inicial</a>

#forms.py
from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome_curso', 'codigo_curso']
        label = {'nome_curso' : '', 'codigo_curso': '' }


#urls.py
path('novo_curso', views.novo_curso, name='novo_curso'),

# views
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CursoForm



def novo_curso(request):
    if request.method != 'POST':
        # Nenhum dado submetido; cria form em branco
        form = CursoForm
    else:
        # Dados de Post submetidos; processa os dados
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gestoreventos:index'))
    context = {'form': form}
    return render(request, 'gestoreventos/novo_curso.html', context)

# novo_curso.html
{% extends "gestoreventos/base.html" %}

{% block content %}

<p>Adicionar novo cursos</p>

<form action="{% url 'gestoreventos:novo_curso' %}" method='post'>
    {% csrf_token %}
    {{ form.as_p }}
    <button name='submit'> Adicionar Curso</button>
</form>

{% endblock content %}
