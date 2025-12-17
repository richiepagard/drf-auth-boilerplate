from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from accounts.utils import get_tokens_for_user
from .wrapper_methods import user_response_data


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    User registration serialization. Model serializer to override 'create' method.
    """
    password2 = serializers.CharField(write_only=True)  # Confirm password

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    default_error_messages = {
        "password_mismatch": _("Passwords must match.")
    }

    def validate(self, attrs: dict) -> dict:
        """
        Ensure that the two entered passwords match.
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(self.default_error_messages["password_mismatch"])

        return attrs

    def create(self, validated_data: dict) -> User:
        """
        Create a new user instance (new rudimentary user) with the given validated data.
        """
        validated_data.pop("password2")

        # Create and save a new User instance
        # with validated data such as username, email, and nickname
        user = User(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
        )
        # Hash the valdiated password data
        user.set_password(validated_data.get("password"))
        user.save()

        self.user = user
        self.tokens = get_tokens_for_user(user)

        return user

    def get_response_data(self, *args, **kwargs):
        """
        Just call the wrapper function to return proper data.
        """
        return user_response_data(self.user, self.tokens)
