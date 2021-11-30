from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http.response import JsonResponse
from ..modelsDB.Product import *
from django.core.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False)
    class Meta:
        model = Product
        fields = ('productID', 'productType', 'productName', 'description', 'stock', 'price', 'img')
