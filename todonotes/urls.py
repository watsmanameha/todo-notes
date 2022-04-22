from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from todo.views import TodoViewSet, ProjectViewSet
from users.views import UserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Todo Notes",
        default_version='0.1',
        description="'Todo Notes' documentation",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('todos', TodoViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/users/0.1', include('users.urls', namespace='0.1')),
    path('api/users/0.2', include('users.urls', namespace='0.2')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]

