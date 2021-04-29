from django.urls import path
from . import views

app_name = 'gestoreventos'

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    path('cursos', views.cursos, name='cursos'),
    path('novo_curso', views.novo_curso, name='novo_curso'),
    path('edit_curso/<int:edit_id>', views.edit_curso, name='edit_curso'),
]
