"""my_p URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from job import urls

schema_view = get_schema_view(
    openapi.Info(
        title="CMDB API",
        default_version='v1',
        description="个人系统API接口文档",
        terms_of_service="https://www.shuaibo.wang/",
        contact=openapi.Contact(email="mail@shuaibo.wang"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(),
    authentication_classes=(),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_doc/', schema_view.with_ui('redoc', cache_timeout=0), name="CMDB API"),
    # rest_framework
    path('', include(urls)),
    # path('', include('job.urls')),
    # django
    url(r'^', include('book.urls'))
]
