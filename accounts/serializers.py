from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)  # Confirm password

    class Meta:
        model = User
        fields = ['username', 'email', 'nickname', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        """
        Ensure that the two entered passwords match.
        """
        if data['password'] != data['password2']:
            raise serializers.ValidationError(_("Passwords must match."))
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove extra fields before saving
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    """
    Custom user login serializer.

    Authenticate user using the provided username and password.
    If authenticate is successful and the user is active, returns a new JWT token pair.
    """
    username = serializers.CharField(
        max_length=30,
        required=True
    )
    password = serializers.CharField(
        required=True,
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username', '').strip()
        password = attrs.get('password')

        # Authenticate user credentials
        user = authenticate(username=username, password=password)

        # Invalid credentials
        if not user:
            raise serializers.ValidationError(_("Invalid login credentials."))

        # Inactive account
        if not user.is_active:
            raise serializers.ValidationError(_("User account is disabled."))

        # Generate a new token for the user
        refresh = RefreshToken.for_user(user)

        return {
            'user': {
                'username': user.username,
                'email': user.email,
                'nickname': getattr(user, 'nickname', '')  # Get user's nickname if it has, otherwise return none string
            },
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
