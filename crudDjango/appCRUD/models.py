from django.db import models

class Usuarios(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    senha = models.TextField(max_length=200)