from demanda.models import Demanda
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import DemandaSerializer


class DemandaViewSet(ModelViewSet):
    serializer_class = DemandaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication)

    def get_queryset(self):
        return Demanda.objects.filter(status=True)
    
    @action(methods=['patch'], detail=True)
    def finalizar_demanda(self, request, *args, **kwargs):

        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)
