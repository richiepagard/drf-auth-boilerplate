from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserLogoutSerializer(serializers.Serializer):
    """
    Blacklists a provided refresh token to log the user out server-side.
    Intended for JWT authentication setups using SimpleJWT.
    """
    refresh = serializers.CharField()

    def validate(self, attrs: dict) -> dict:
        """
        Validates the incoming serializer data.
        Extracts and stores the submitted refresh token.

        Args:
            attrs (dict): Incoming serializer data containing the refresh token.

        Returns:
            dict: The validated serializer data.
        """
        self.token = attrs["refresh"]

        return attrs

    def save(self, **kwargs: dict):
        """
        Attempts to blacklist the token.
        Fails if the token is invalid or unusable.

        Raises:
            TokenError: If the token is invalid, expired, or cannot be blacklisted.
        """
        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail("bad_token")
