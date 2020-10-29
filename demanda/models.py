# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from endereco.models import Endereco

class Demanda(models.Model):
    descricao_peca = models.CharField(max_length=150, null=False, blank=False)
    endereco_entrega = models.ForeignKey(
        Endereco, on_delete=models.SET('Endereco Removido'))
    informacoes_contato = models.TextField(null=False, blank=False)
    anunciante = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return self.descricao_peca
