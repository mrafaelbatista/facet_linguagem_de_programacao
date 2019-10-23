from django.db import models

# Create your models here.

class Assunto(models.Model):
    """Um assunto sobre qual o usuário que ser ouvido"""

    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Devolve uma representação string do modelo """
        return self.text