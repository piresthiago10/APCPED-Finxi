from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from demanda.models import Demanda
from .serializers import DemandaSerializer

class DemandaViewSet(ModelViewSet):
    serializer_class = DemandaSerializer

    def def get_queryset(self):
        return Demanda.objects.all()
    