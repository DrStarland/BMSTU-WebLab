
from ..permissions import IsOwnerOrReadOnly, IsCurrentUserOrReadOnly
from rest_framework import permissions
from ..myapi import AutismSchema as AutoSchema
from ..repositories.unit_of_work import DjangoUnitOfWork_Transaction
from ..business_logic.objects.Transaction import Transaction_bl
from ..DTOs.TransactionSerializer import *
from .BaseAPIView import BaseAPIView

from rest_framework.response import Response

from datetime import date

from .ProductAPIView import ProductAPIView 
from ..business_logic.objects.Member import Member_bl

class TransactionsAPIView(BaseAPIView):
    '''
    Заказы, созданные участниками.
    Поля: IDзаказа, IDучастника, IDтоваров, количества_товаров, статус, дата.
    '''

    unit_of_work = DjangoUnitOfWork_Transaction
    bl_model = Transaction_bl
    serializer_class = TransactionSerializer

    schema = AutoSchema(
        tags=['Заказы'],
    )

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к заказам запросы.
        '''
        if self.action in ('retrieve', 'create', 'partial_update'):
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        else:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

    def create(self, request, *args, **kwargs):
        params, serializer = self.getDataFromRequest(request, **kwargs)
        
        memba = Member_bl(memberID=request.user.id)
        #params['memberID'] = memba.get_absolute_url()
        params['transactionDate'] = date.today()
        with self.unit_of_work() as uow:
            uow.stored_model.add( self.bl_model(args = params) )
            uow.commit()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
