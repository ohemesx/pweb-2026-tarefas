from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    prazo = models.DateField()

    def __str__(self):
        return self.nome
