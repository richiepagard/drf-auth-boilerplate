from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import UserRegisterView


app_name = 'accounts'

AUTH_URLS = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
]
JWT_URLS = [
    # Generate access and refresh tokens for user login
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    # Refresh access token using a valid refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]

urlpatterns = AUTH_URLS + JWT_URLS
