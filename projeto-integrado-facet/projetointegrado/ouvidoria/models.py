from django.db import models

# Create your models here.
class Topico(models.Model):
    assunto_topico = models.CharField(max_length=50)

class Postit(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.PROTECT)
    assunto = models.CharField(max_length=50)
    texto = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)


