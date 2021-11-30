from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http.response import JsonResponse

from ..modelsDB.Comment import *

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('productID', 'message', 'commentDate',)
