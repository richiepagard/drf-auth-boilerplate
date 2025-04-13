from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
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


class UserLogoutView(APIView):
    """
    Log out a user by blacklisting their refresh token.

    Requires the user to be authenticated and sends the refresh token in the request body.
    On success, the refresh token is blacklisted, preventing further use for token refresh.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Extract refresh token from request data
            refresh_token = request.data.get('refresh')

            # Ensure refresh token exists, else raise custom exception
            if not refresh_token:
                return Response(
                    {'error': 'Refresh token is required.'},
                    status = status.HTTP_400_BAD_REQUEST
                )

            # Create a token object and blacklist it
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {'message': 'You have successfully logged out.'},
                status=status.HTTP_205_RESET_CONTENT
            )

        except Exception as e:
            # If token is invalid or missing, return a bad request
            return Response(
                {'error': 'Invalid or missing refresh token.'},
                status=status.HTTP_400_BAD_REQUEST
            )
