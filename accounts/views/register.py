from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import UserRegisterSerializer


class UserRegisterView(APIView):
    """
    User registration view!

    Requests:
        POST (HTTP): Gets validated data from the client and register a new user.

    Returns:
        dict: Use information such as validated data, access, and refresh tokens fro authentication.
    """
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Keeps serializer return data in the 'user' for response
        user = serializer.get_response_data()

        return Response(
            data=user,
            status=status.HTTP_201_CREATED
        )
