from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import UserRegisterSerializer, UserLoginSerializer


class UserRegisterView(APIView):
    """
    View for registration a new user and returning JWT tokens.

    Methods:
        post(request): Validation and registers a new user. Returns user data and tokens on success.
    """

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)  # Generate JWT token for the new user

            return Response(
                {
                    'user': serializer.data,  # User information will return
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    """
    User login view.

    Accepts username and password via POST request.
    Validate the credentials using a custom login serializer.
    If authenticate is successful, returns a pair of JWT tokens along with basic user info.
    """

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        # Validate the input; raise an exception and return 400 if invalid
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
