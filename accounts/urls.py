from django.urls import path

from accounts.views import (
    # Authentication
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    # User Profie
    UserProfileRetrieveView,
    UserPorfileUpdateView,
    # JWT Tokens
    AuthTokenObtainPairView,
    AuthTokenRefreshView
)


app_name = 'accounts'

USER_AUTH_URLS = [
    path('users/register/', UserRegisterView.as_view(), name='user-register'),
    path('users/login/', UserLoginView.as_view(), name='user-login'),
    path('users/logout/', UserLogoutView.as_view(), name='user-logout'),
]
USER_PROFILE_URLS = [
    path(
        "users/<int:user_pk>/profile/",
        UserProfileRetrieveView.as_view(),
        name="user-profile"
    ),
    path(
        "users/profile/update/",
        UserPorfileUpdateView.as_view(),
        name="user-profile-update"
    )
]
JWT_URLS = [
    # Generate access and refresh tokens for user login
    path('token/', AuthTokenObtainPairView.as_view(), name='token-obtain-pair'),
    # Refresh access token using a valid refresh token
    path('token/refresh/', AuthTokenRefreshView.as_view(), name='token-refresh'),
]

urlpatterns = USER_AUTH_URLS + USER_PROFILE_URLS + JWT_URLS
