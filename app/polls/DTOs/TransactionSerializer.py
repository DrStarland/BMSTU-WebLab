from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from ..modelsDB.Transaction import *
from django.http.response import JsonResponse

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transactionID', 'productIDs', 'productQuantities',
                    'approvalStatus', 'transactionDate')
    