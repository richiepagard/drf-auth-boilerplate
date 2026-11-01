from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

SPECTACULAR_URLS = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # UI
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]

ADMIN_URLS = [
    path("admin/", admin.site.urls)
]
AUTH_URLS = [
    # JWT & future login/register APIs
    path('api/auth/', include('accounts.urls', namespace='accounts')),
]
COMMON_URLS = [
    path("", include("common.urls", namespace="common")),
]

APPS_ENDPOINTS = AUTH_URLS + COMMON_URLS
urlpatterns = ADMIN_URLS + APPS_ENDPOINTS + SPECTACULAR_URLS
