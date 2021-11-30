from rest_framework import permissions
from ..DTOs.UserSerializer import *
from ..permissions import IsCurrentUserOrReadOnly
from ..myapi import AutismSchema as AutoSchema
from ..repositories.unit_of_work import DjangoUnitOfWork_Member
from ..business_logic.objects.Member import Member_bl
from .BaseAPIView import BaseAPIView

class UserAPIView(BaseAPIView):
    '''
    Участники (пользователи), зарегистрированные на сайте.
    Поля: ID, логин, пароль.
    (опционально - другие персональные данные)
    '''
    schema = AutoSchema(
        tags=['Участники'],
    )

    unit_of_work = DjangoUnitOfWork_Member
    bl_model = Member_bl
    serializer_class = UserSerializer

    def get_serializer_class(self):
        '''
        Функция определения сериалайзера.
        '''
        return self.serializer_class

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к списку участников запросы.
        '''
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsCurrentUserOrReadOnly()]
        elif self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

