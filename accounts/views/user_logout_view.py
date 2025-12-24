from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from accounts.serializers import UserLogoutSerializer


class UserLogoutView(APIView):
    """
    Accepts a refresh token and blacklists it to log the user out.
    Requires JWT authentication with SimpleJWT blacklist enabled.

    Requests:
        POST (HTTP).

    Returns:
        205 Reset Content indicating successful logout or validation failure.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Handles logout by validating and blacklisting the provided refresh token.
        """
        serializer = UserLogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # NOTE: 205 suggests the client should reset the view (tokens cleared client-side).
        return Response(
            {"detail": "Logged out successfully"},
            status=status.HTTP_205_RESET_CONTENT
        )
