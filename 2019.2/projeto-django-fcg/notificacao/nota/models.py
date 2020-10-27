from django.db import models

# Create your models here.

class Nota(models.Model):
    texto = models.TextField(max_length=500)