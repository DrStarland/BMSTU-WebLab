from rest_framework import permissions
from ..myapi import AutismSchema as AutoSchema
from ..repositories.unit_of_work import DjangoUnitOfWork_Product
from ..business_logic.objects.Product import Product_bl
from ..DTOs.ProductSerializer import *

from .BaseAPIView import BaseAPIView


class ProductAPIView(BaseAPIView):
    '''
    Товары, хранящиеся в каталоге.
    Поля: ID, тип, название, описание, количество в наличии, цена, изображение (опционально).
    '''

    unit_of_work = DjangoUnitOfWork_Product   
    bl_model = Product_bl 
    serializer_class = ProductSerializer

    schema = AutoSchema(
        tags=['Товары'],
    )

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к каталогу товаров запросы.
        '''
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]