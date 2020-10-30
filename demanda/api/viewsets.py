from demanda.models import Demanda
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwnerOrReadOnly
from .serializers import DemandaSerializer


class DemandaViewSet(ModelViewSet):
    serializer_class = DemandaSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        """[Exibe apenas as demandas não finalizadas]

        Returns:
            [filter]: [demandas com os status True]
        """
        return Demanda.objects.filter(status=True)
    
    @action(methods=['patch'], detail=True)
    def finalizar_demanda(self, request, *args, **kwargs):
        """[Alteração do status de uma demanda]

        Args:
            request ([request]): [requisição http]

        Returns:
            [metodo]: [atualização parcial de uma demanda]
        """
        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """[Cria uma nova demanda]

        Args:
            request ([request]): [requisição http]

        Returns:
            [Response]: [dados da nova demanda, status http e headers]
        """
        request.data['anunciante'] = request.user.pk
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """[Atualiza uma requisição]

        Args:
            request ([request]): [requisição http]

        Returns:
            [type]: [dados da demanda atualizada]
        """
        request.data['anunciante'] = request.user.pk
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    

