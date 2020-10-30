# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Demanda
from django.utils.html import format_html


@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):

    actions_on_top = True
    actions_on_bottom = True
    raw_id_fields = ('endereco_entrega', 'anunciante',)
    list_display = ('descricao_peca', 'endereco_entrega',
                    'informacoes_contato', 'anunciante', 'sobrescrita_status')

    def sobrescrita_status(self, obj):
        """[Adiciona na lista de demandas uma coluna que exibe icones de acordo com o status da demanda.]

        Args:
            obj ([object]): [Objeto da classe Demanda]

        Returns:
            [format_html]: [formatação para inserir imagem de status]
        """

        if obj.status == True:
            return format_html("<img src='/media/baseline-check_circle_outline.svg'/>")
        else:
            return format_html("<img src='/media/baseline-highlight_off.svg'/>")

    sobrescrita_status.short_description = "status"