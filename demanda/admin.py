# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Demanda


@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    raw_id_fields = ('endereco_entrega', 'anunciante',)

    list_display = ('descricao_peca', 'endereco_entrega', 'informacoes_contato', 'anunciante', 'status')
