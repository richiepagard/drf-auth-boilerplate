from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from accounts.views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView
)

app_name = 'accounts'

jwt_urlpatterns = [
    # Generate access and refresh tokens for user login
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    # Refresh access token using a valid refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
auth_urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout')
]
urlpatterns = jwt_urlpatterns + auth_urlpatterns
