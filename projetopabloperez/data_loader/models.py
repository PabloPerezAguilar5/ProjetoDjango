from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    dados_adicionais = models.JSONField(blank=True, null=True)
    stock = models.IntegerField() 


    def __str__(self):
        return self.nome
