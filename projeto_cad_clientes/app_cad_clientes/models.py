from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    endereco = models.TextField(max_length=100)
    aparelho = models.TextField(max_length=100)
    problema = models.TextField(max_length=100)
    valor_pecas = models.IntegerField()
    mao_de_obra = models.IntegerField()
    total_servico = models.IntegerField()
    pediu_nota = models.TextField(max_length=30)