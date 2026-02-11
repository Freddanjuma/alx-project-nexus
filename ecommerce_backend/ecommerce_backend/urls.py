from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet
from categories.views import CategoryViewSet

# JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


# Router
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)


# Swagger configuration
schema_view = get_schema_view(
    openapi.Info(
        title="E-commerce API",
        default_version='v1',
        description="API documentation for the e-commerce backend",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes
    path('api/', include(router.urls)),
    path('api/users/', include('users.urls')),
    path('api/auth/', include('rest_framework.urls')),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
