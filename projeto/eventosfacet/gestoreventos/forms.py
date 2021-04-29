from django import forms

from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome_curso', 'codigo_curso']
        label = {'nome_curso' : '', 'codigo_curso' : ''}