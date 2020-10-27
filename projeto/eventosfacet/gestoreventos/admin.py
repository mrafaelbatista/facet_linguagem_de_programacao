from django.contrib import admin

# Import dos modelos
from gestoreventos.models import Curso, Funcionario

# Register your models here.
admin.site.register(Curso)
admin.site.register(Funcionario)
