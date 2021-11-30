#from .serializers import *


'''
Django ViewSet actions:
list -- GET - список
retrieve -- GET - одну запись
create -- POST
update -- PUT
partial_update -- PATCH - обновление частичное (1 поле, например)
destroy -- DELETE
'''

from .API_views.ProductAPIView import *
from .API_views.ProductTypeAPIView import *
from .API_views.UserAPIView import *
from .API_views.CommentsAPIView import *
from .API_views.RatingsAPIView import *
from .API_views.TransactionAPIView import *
from .API_views.CartAPIView import *

# бесполезные декораторы, которые не помогают
# from rest_framework.decorators import api_view
# from drf_yasg.utils import swagger_auto_schema
# from django.utils.decorators import method_decorator
# from rest_framework.decorators import action
