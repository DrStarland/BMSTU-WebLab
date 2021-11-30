from rest_framework import permissions, serializers, status, viewsets
from rest_framework.response import Response
from abc import abstractmethod
from .common import CommonMixin

class BaseAPIView(viewsets.ModelViewSet, CommonMixin):
    '''
    Базовый класс для используемых в приложении View
    '''
    #   viewsets.ModelViewSet: a viewset that provides default `create()`,
    #       `retrieve()`, `update()`, `partial_update()`, `destroy()`
    #       and `list()` actions
    serializer_class = None     # сериализатор вашей модели
    unit_of_work = None         # используемый класс UnitOfWork
    bl_model = None             # ключевой класс бизнес-логики
    # schema = AutoSchema(      # это необходимо определить в каждой модели
    #     tags=['Пример названия на странице api'],
    # )

    @abstractmethod
    def get_permissions(self):
        raise NotImplementedError

    def get_serializer_class(self):
        return self.serializer_class

    def get_queryset(self):
        with self.unit_of_work() as uow:
            bl_queryset = uow.stored_model.list()
            uow.commit()
        return bl_queryset

    def get_object(self, searched_ID = None):
        if not searched_ID:
            searched_ID = self.getIDfromUrl()
        with self.unit_of_work() as uow:
            obj = uow.stored_model.get(searched_ID)
            uow.commit()
        return obj

    def destroy(self, request, *args, **kwargs):
        with self.unit_of_work() as uow:
            uow.stored_model.delete( self.get_object() )
            uow.commit()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        validata = {**serializer.validated_data, **kwargs}
        obj.updateFromDict(validata)
        with self.unit_of_work() as uow:
            uow.stored_model.update(obj)
            uow.commit()

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def getDataFromRequest(self, request, **kwargs):
        """
        Возвращает в виде кортежа из двух элементов преобразованный в стандартный Python-
        словарь данные, содержащиеся в запросе, а также связанный с ними сериализатор.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data, '\n', serializer.initial_data)
        # позволяет переработать ордеред дикт в простой словарь
        return {**serializer.validated_data, **kwargs}, serializer

    def create(self, request, *args, **kwargs):
        params, serializer = self.getDataFromRequest(request, **kwargs)
        with self.unit_of_work() as uow:
            uow.stored_model.add( self.bl_model(args = params) )
            uow.commit()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)









r"""
⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢾
⠀⠀⠀⠀⠀⡐⢕⠊⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⢳
⠀⠀⠀⠀⢰⢕⡇⠀⢀⡞⠙⢆⠀⠀⢀⣀⣀⣠⠶⠛⠉⠀⠀⠀⠙⢦
⠀⠀⠀⠀⢸⢕⡇⠀⣸⠀⠀⠀⠉⠒⠚⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳
⠀⠀⠀⠀⢸⢕⠗⠉⠏⠀⢀⡀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠔⠁⠀⢀⠃
⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠈⠁⠤⣆⠪⠸⠀⠒⠂⠜⠒⠀⠀⣠⠞⢷
⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠚⠲⠶⡤⡤⠔⡈⢧⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣶⣶⣶⡾
⠀⠀⠀⠀⠀⠙⠛⠉⠑⠒⠢⠤⣾⡷⠓⢾⡷⠈⢾⣷⠒⠒⢾⣷⠊⠉⠉⠉⠉
"""

        # list_products = self.queryset
        # # print(list_products.values())
        # query = self.request.query_params.get('favourite')
        # user = self.request.user
        # print(query)
        # if (query is not None and user is not None):
        #     print("Huuh?")
        #     list_products = list_products.in_bookmarks(self.request.user)
        # return list_products