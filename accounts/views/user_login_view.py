from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import UserLoginSerializer


class UserLoginView(APIView):
    """
    Login user view!

    Requests:
        POST (HTTP): Gets client data and validate them to authenticate the user.

    Returns:
        dict: User information such as validated data, access, and refresh tokens for authentication.
    """
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        # Keeps serializer return data in the 'user' for response
        user = serializer.get_response_data()

        return Response(
            data=user,
            status=status.HTTP_202_ACCEPTED
        )
