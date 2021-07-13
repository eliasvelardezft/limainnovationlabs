from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Client, CreditRequest
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'sbs_debt',
            'sentinel_risk_score'
        ]
        
class CreditRequestSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = CreditRequest
        fields = [
            'id',
            'date',
            'amount',
            'status',
            'ai_score',
            'cliente'
        ]

