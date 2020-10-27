from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from demanda.models import Demanda
from .serializers import DemandaSerializer
from rest_framework.decorators import action 

class DemandaViewSet(ModelViewSet):
    serializer_class = DemandaSerializer

    def get_queryset(self):
        return Demanda.objects.all()
    
    @action(methods=['patch'], detail=True)
    def finalizar_demanda(self, request, *args, **kwargs):

        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)