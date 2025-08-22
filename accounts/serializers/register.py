from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from accounts.utils import get_tokens_for_user


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    User registration serialization. Model serializer to override 'create' method.
    """
    password2 = serializers.CharField(write_only=True)  # Confirm password

    class Meta:
        model = User
        fields = ['username', 'email', 'nickname', 'password', 'password2']
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
            nickname=validated_data.get("nickname")
        )
        # Hash the valdiated password data
        user.set_password(validated_data.get("password"))
        user.save()

        self.user = user
        self.tokens = get_tokens_for_user(user)

        return user

    def get_response_data(self, *args, **kwargs) -> dict:
        """
        Calling it after 'is_valid()' method in views
        to done the user registration process.

        Returns user information includes user tokens for authentication.
        """
        user_info = {
            "user_id": self.user.pk,
            "username": self.user.username,
            "email": self.user.email,
            "nickname": self.user.nickname,
            "tokens": self.tokens
        }

        return user_info
