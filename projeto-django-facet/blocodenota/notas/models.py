from django.db import models

# Create your models here.

class Nota(models.Model):
    texto_nota = models.CharField(max_length=500)