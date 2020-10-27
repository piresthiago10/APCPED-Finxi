from demanda.models import Demanda
from rest_framework.serializers import ModelSerializer


class DemandaSerializer(ModelSerializer):
    class Meta:
        model = Demanda
        fields = ('id', 'descricao_peca', 'endereco_entrega', 'informacoes_contato',
                  'anunciante', 'status')
