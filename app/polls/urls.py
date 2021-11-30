from django.http.response import HttpResponse
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.conf.urls import url
from . import serializers

router = routers.DefaultRouter()

basenames = { 'Products' : 'product', 'ProductTypes' : 'producttype', 'Members' : 'user', 'Comments' : 'comment',
    'Ratings' : 'rating', 'Transactions' : 'transaction', 'Carts' : 'cart' }

router.register('Products', views.ProductAPIView, basenames['Products'])
router.register('ProductTypes', views.ProductTypeAPIView, basenames['ProductTypes'])
router.register('Members', views.UserAPIView, basenames['Members'])
router.register('Comments', views.CommentsAPIView, basenames['Comments'])
router.register('Ratings', views.RatingsAPIView, basenames['Ratings'])
router.register('Transactions', views.TransactionsAPIView, basenames['Transactions'])
router.register('Carts', views.CartsAPIView, basenames['Carts'])

# user_one = views.UserAPIView.as_view({
#     'get': 'retrieve'
# })

urlpatterns = [
   # url(r'^Products/(?P<pk>[0-9]+)$', serializers.products_list),
    path('openapi', get_schema_view(
        title="-=Shop for artists=-",
        description="Best API ever",
        version="0.0.3"
    ), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('', include(router.urls)),
]
