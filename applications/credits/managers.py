from django.db import models
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.authtoken.models import Token


class ClientManager(models.Manager):

    def hola(self):
        print("hola")
    




class CreditRequestManager(models.Manager):

    def hola(self):
        print("hola")


