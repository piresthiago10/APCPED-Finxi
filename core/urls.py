from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from demanda.api.viewsets import DemandaViewSet


router = routers.DefaultRouter()
router.register(r'demandas', DemandaViewSet, basename='Demanda')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
