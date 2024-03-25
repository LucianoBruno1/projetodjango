from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    idade = models.IntegerField()
    nome = models.TextField(max_length=255)
