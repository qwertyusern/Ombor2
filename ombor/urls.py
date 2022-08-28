from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from asosiy.views import *
from stats.views import *
from userapp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Ombor API",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact("Xojiakbar Goipov. xojiakbargoipov3@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc'),
    path('mahsulotlar/',MahsulotApiView.as_view()),
    path('mahsulot/<int:pk>/',MahsulotApi.as_view()),
    path('clientlar/', ClientApiView.as_view()),
    path('client/<int:pk>/', ClientApi.as_view()),
    path('stats/', StatsApiView.as_view()),
    path('stat/<int:pk>/', StatsApi.as_view()),
    path('ombor/<int:pk>/', OmborApi.as_view()),
    path('userlar/', Userlar.as_view()),
    path('user/<int:pk>', UserV.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]






