from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from utility import views
from travelando import settings

router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(r'query_selection/', views.QuerySelectionView.as_view(), name='searches_process'),
    path(r'templates/', views.TemplateSelectionView.as_view(), name='searches_process'),
]
