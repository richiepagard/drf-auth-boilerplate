from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Auth - Token"])
class AuthTokenObtainPairView(TokenObtainPairView):
    """
    Just overriding the Token Obtain Pair View
    to add it in the specific tags list of schema
    and some customizations if needed.
    """
    pass


@extend_schema(tags=["Auth - Token"])
class AuthTokenRefreshView(TokenRefreshView):
    """
    Just overriding the Token Refresh View
    to add it in the specific tags list of schema
    and some customizations if needed.
    """
    pass
