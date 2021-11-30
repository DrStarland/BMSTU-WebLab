"""webmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
# from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('api/v1/', include('polls.urls')),
    path('admin/', admin.site.urls),
    # path('legacy/', include('polls.urls')), # potom izmenitsya
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('api-token-auth/', obtain_jwt_token),
    url('api-token-refresh/', refresh_jwt_token),
    url('api-token-verify/', verify_jwt_token),
]
#urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
