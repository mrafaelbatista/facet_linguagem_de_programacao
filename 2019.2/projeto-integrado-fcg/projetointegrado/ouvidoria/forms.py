from django import forms
from .models import Assunto


class AssuntoForm(ModelForm):
    class Meta:
        model = Assunto
        fields = ['text']
        labels = {'text':''}
