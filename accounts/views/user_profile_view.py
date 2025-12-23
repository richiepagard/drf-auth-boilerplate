from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from accounts.serializers import (
    UserProfileRetrieveSerializer,
    UserProfileUpdateSerializer
)
from accounts.models import User


class UserProfileRetrieveView(APIView):
    """
    Showing user profile including user's public information.

    Requests:
        GET (HTTP).

    Returns:
        404 Not Found if the user instance with the given PK does not exist.
        200 OK the user profile info returns as data.
    """
    serializer_class = UserProfileRetrieveSerializer

    def get(self, request, user_pk: int):
        """
        Gets user profile by user's PK and shows its profile info.

        Args:
            user_pk (int): The user's PK the profile belongs to.
        """
        user = get_object_or_404(User, pk=user_pk)
        user_profile = user.userprofile
        serializer = self.serializer_class(instance=user_profile)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )


class UserPorfileUpdateView(APIView):
    """
    Lets users update/edit their own profile.

    Requests:
        PATCH (HTTP).

    Returns:
        202 Accepted if the serializer data valid and updated user profile properly.
    """
    serializer_class = UserProfileUpdateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_object(self):
        """
        Ensures each user can only update its own profile.
        """
        return self.request.user.userprofile

    def patch(self, request, *args, **kwargs):
        """
        Supporting PATCH HTTP method to allowed
        partial updates.
        """
        profile = self.get_object()
        serializer = self.serializer_class(
            instance=profile,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_202_ACCEPTED
        )
