from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from accounts.utils import get_tokens_for_user
from .wrapper_methods import user_response_data


class UserLoginSerializer(serializers.Serializer):
    """
    User login serialization. Validated user and authenticated it.

    Authenticate user using the provided username and password.
    If authenticate is successful and the user is active,
    returns a new JWT token pair.
    """
    username = serializers.CharField(
        max_length=30,
        required=True
    )
    password = serializers.CharField(
        required=True,
        write_only=True
    )

    default_error_messages = {
        "missing_fields": _("Both username and password are required."),
        "invalid_credentials": _("Invalid login credentials."),
        "inactive_account": _("User account is disabled.")
    }

    def validate(self, attrs: dict) -> dict:
        """
        Authenticate and validate user.
        Validation for username and password fields.

        Exceptions:
            ValidationError if username or password is empty.
            ValidationError if authenticated user is None.
            ValidationError if user does not an active user.

        Returns:
            dict: If the data validated successfully and user authenticated,
                it contains user data.
        """
        
        username = attrs.get('username', '').strip()
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError(
                self.default_error_messages["missing_fields"]
            )

        # Authenticate user
        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                self.default_error_messages["invalid_credentials"]
            )

        if not user.is_active:
            raise serializers.ValidationError(
                self.default_error_messages["inactive_account"]
            )

        # Store user to using it in other methods
        self.user = user
        self.tokens = get_tokens_for_user(self.user)
        # Updates 'attrs' to store user info
        attrs["user"] = user
        return attrs

    def get_response_data(self, *args, **kwargs):
        """
        Just call the wrapper function to return proper data.
        """
        return user_response_data(self.user, self.tokens)
