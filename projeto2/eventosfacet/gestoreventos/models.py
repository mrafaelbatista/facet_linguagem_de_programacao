from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    codigo_curso = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome_curso

class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=150)
    matricula = models.IntegerField()
    email_institucional = models.CharField(max_length=100)
    curso_vinculado = models.ForeignKey(Curso, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome_funcionario

class Palestrante(models.Model):
    nome_palestrante = models.CharField(max_length=150)
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False)
    cpf = models.CharField(max_length=11)
    email_palestrante = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_palestrante

class Evento(models.Model):
    nome_evento = models.CharField(max_length=200)
    data_inicio = models.DateTimeField(auto_now=False, auto_now_add=False)
    data_final = models.DateTimeField(auto_now=False, auto_now_add=False)
    curso_organizador = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    palestrantes = models.ForeignKey(Palestrante, on_delete=models.RESTRICT)
    organizador = models.ForeignKey(Funcionario, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome_evento