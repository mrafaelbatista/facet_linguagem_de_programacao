from django.db import models

# Create your models here.

class Assunto(models.Model):
    tx_assunto = models.CharField(max_length=100)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tx_assunto