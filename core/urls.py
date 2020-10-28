from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from demanda.api.viewsets import DemandaViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'demandas', DemandaViewSet, basename='Demanda')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
