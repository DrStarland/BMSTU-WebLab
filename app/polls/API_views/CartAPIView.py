from rest_framework import permissions
from ..DTOs.CartSerializer import *
from ..permissions import IsOwnerOrReadOnly
from ..myapi import AutismSchema as AutoSchema
from ..repositories.unit_of_work import DjangoUnitOfWork_Cart
from ..business_logic.objects.Cart import Cart_bl
from .BaseAPIView import BaseAPIView

class CartsAPIView(BaseAPIView):
    '''
    Корзина, принадлежащая участнику и позволяющая хранить товары из каталога для совершения заказа.
    Поля: IDкорзина, IDучастника, IDтоваров, количества_товаров, количество_видов_товаров.
    '''
    schema = AutoSchema(
        tags=['Корзины'],
    )

    unit_of_work = DjangoUnitOfWork_Cart  
    bl_model = Cart_bl
    serializer_class = CartSerializer

    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к корзине запросы.
        '''
        if self.action in ('retrieve', 'create', 'partial_update'):
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        else:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]


