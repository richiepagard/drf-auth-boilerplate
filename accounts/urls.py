from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from accounts.views import UserRegisterView, UserLoginView

app_name = 'accounts'

jwt_urlpatterns = [
    # Generate access and refresh tokens for user login
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Refresh access token using a valid refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
auth_urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
]
urlpatterns = jwt_urlpatterns + auth_urlpatterns
