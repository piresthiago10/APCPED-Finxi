from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from demanda.models import Demanda
from endereco.models import Endereco
from endereco.api.serializers import EnderecoSerializer
from .serializers import DemandaSerializer

class DemandaViewSet(ModelViewSet):
    serializer_class = DemandaSerializer

    def get_queryset(self):
        return Demanda.objects.all()
    
    # def create(self, request, *args, **kwargs):

    #     endereco = request.data
        
    #     return Response(endereco)