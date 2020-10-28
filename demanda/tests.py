# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase

from demanda.api.serializers import DemandaSerializer
from demanda.models import Demanda


class RegistrationTestCase(APITestCase):

