# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length=250)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.logradouro
    
