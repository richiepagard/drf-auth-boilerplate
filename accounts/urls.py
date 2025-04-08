from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

app_name = 'accounts'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # Generate access and refresh tokens for user login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   # Refresh access token using a valid refresh token
]
