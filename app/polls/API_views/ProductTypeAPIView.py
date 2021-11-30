from rest_framework import permissions
from ..myapi import AutismSchema as AutoSchema
from ..DTOs.ProductTypeSerializer import *
from ..repositories.unit_of_work import DjangoUnitOfWork_ProductType
from ..business_logic.objects.ProductType import ProductType_bl
from .BaseAPIView import BaseAPIView

class ProductTypeAPIView(BaseAPIView):
    '''
    Типы товаров.
    Поля: ID, название, описание.
    '''
    schema = AutoSchema(
        tags=['Тип товара'],
    )

    serializer_class = ProductTypeSerializer
    unit_of_work = DjangoUnitOfWork_ProductType   
    bl_model = ProductType_bl 

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к типу товаров запросы.
        '''
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
