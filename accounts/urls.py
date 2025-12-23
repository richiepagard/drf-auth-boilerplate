from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import (
    UserRegisterView,
    UserLoginView,
    # User Profie
    UserProfileRetrieveView,
)


app_name = 'accounts'

USER_AUTH_URLS = [
    path('users/register/', UserRegisterView.as_view(), name='user-register'),
    path('users/login/', UserLoginView.as_view(), name='user-login'),
]
USER_PROFILE_URLS = [
    path(
        "users/<int:user_pk>/profile/",
        UserProfileRetrieveView.as_view(),
        name="user-profile"
    )
]
JWT_URLS = [
    # Generate access and refresh tokens for user login
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    # Refresh access token using a valid refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]

urlpatterns = USER_AUTH_URLS + USER_PROFILE_URLS + JWT_URLS
