from rest_framework import permissions
from ..DTOs.CommentSerializer import *
from ..myapi import AutismSchema as AutoSchema
from ..repositories.unit_of_work import DjangoUnitOfWork_Comment
from ..business_logic.objects.Comment import Comment_bl
from .BaseAPIView import BaseAPIView

class CommentsAPIView(BaseAPIView):
    '''
    Комментарии, оставленные участниками на сайте к определенным товарам.
    Поля: IDкомментария, IDавтора, IDтовара, текст, дата.
    '''
    schema = AutoSchema(
        tags=['Комментарии'],
    )

    unit_of_work = DjangoUnitOfWork_Comment  
    bl_model = Comment_bl
    serializer_class = CommentSerializer

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к комментариям запросы.
        '''
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        elif self.action == 'create':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]