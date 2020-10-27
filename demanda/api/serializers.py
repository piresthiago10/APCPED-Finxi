from demanda.models import Demanda
from endereco.models import Endereco
from endereco.api.serializers import EnderecoSerializer
from usuario.api.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers


class DemandaSerializer(WritableNestedModelSerializer):
    endereco_entrega = EnderecoSerializer()
    anunciante = User.objects.all()

    class Meta:
        model = Demanda
        fields = ('id', 'descricao_peca', 'endereco_entrega', 'informacoes_contato',
                  'anunciante', 'status')


