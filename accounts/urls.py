from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from accounts.views import UserRegisterView

app_name = 'accounts'

jwt_urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # Generate access and refresh tokens for user login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   # Refresh access token using a valid refresh token
]
auth_urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
]
urlpatterns = jwt_urlpatterns + auth_urlpatterns
