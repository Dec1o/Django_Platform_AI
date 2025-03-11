from django.db import models

class Company(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
