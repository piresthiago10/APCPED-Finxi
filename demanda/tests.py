# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import (APIRequestFactory, APITestCase,
                                 force_authenticate)

from demanda.api.serializers import DemandaSerializer
from demanda.models import Demanda


class RegistrationTestCase(APITestCase):

    def setUp(self):
        """[cria um usuario de testes]
        """
        self.user = User.objects.create(username="admin", password="admin")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        """[cria uma credencial Token]
        """
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.token))

    def test_nova_demanda_token(self):
        """[teste de criação de demanda com autenticação]
        """
        data = {
            "descricao_peca": "Propulsor Atômico 153",
            "endereco_entrega": {
                "logradouro": "Rua Planeta",
                "numero": "10",
                "bairro": "Liberdade",
                "cidade": "São Paulo",
                "estado": "São Paulo",
                "cep": "23847-985"
            },
            "informacoes_contato": "nenhuma",
            "status": True
        }

        self.api_authentication()
        response = self.client.post("/demandas/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_demandas(self):
        """[teste de retorno de demanda com autorização]
        """
        self.api_authentication()
        response = self.client.get("/demandas/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_demanda_not_found(self):
        """[teste de acesso a um endpoint que não existe]
        """
        self.api_authentication()
        response = self.client.get("/demandas/133/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class RegistrationTestCaseNoToken(APITestCase):

    def test_nova_demanda_sem_token(self):
                """[teste de criação de demanda sem autenticação]
        """
        data = {
            "descricao_peca": "Propulsor Atômico 153",
            "endereco_entrega": {
                "logradouro": "Rua Planeta",
                "numero": "10",
                "bairro": "Liberdade",
                "cidade": "São Paulo",
                "estado": "São Paulo",
                "cep": "23847-985"
            },
            "informacoes_contato": "nenhuma",
            "status": True
        }

        response = self.client.post("/demandas/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_demanda_sem_token(self):
        """[teste de retorno de demanda sem autorização]
        """
        response = self.client.get("/demandas/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
