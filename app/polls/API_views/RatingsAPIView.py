
from ..permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from ..myapi import AutismSchema as AutoSchema
from ..DTOs.RatingSerializer import *
from ..DTOs.RatingUpdateSerializer import *
from ..repositories.unit_of_work import DjangoUnitOfWork_Rating
from ..business_logic.objects.Rating import Rating_bl
from .BaseAPIView import BaseAPIView

class RatingsAPIView(BaseAPIView):
    '''
    Оценки, оставленные участниками на сайте к определенным товарам.
    Поля: IDоценки, IDавтора, IDтовара, значение.
    '''
    schema = AutoSchema(
        tags=['Оценки'],
    )

    serializer_class = RatingSerializer
    unit_of_work = DjangoUnitOfWork_Rating   
    bl_model = Rating_bl     

    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к оценкам запросы.
        '''
        if self.action in ('list', 'retrieve', 'create', 'partial_update'):
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

    def get_serializer_class(self):
        '''
        Функция определения сериалайзера.
        '''
        # if self.action == 'update':
        #     return RatingUpdateSerializer
        return RatingSerializer
