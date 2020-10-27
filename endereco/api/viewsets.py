from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from endereco.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer