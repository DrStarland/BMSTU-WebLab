from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http.response import JsonResponse

from ..modelsDB.Product import *

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
   # typeName = serializers.CharField(source='producttype.typeName', read_only=True)
    class Meta:
        model = ProductType
        fields = ('typeID', 'typeName', 'description')