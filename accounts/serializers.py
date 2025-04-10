from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

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
        validated_data.pop('password2') # Remove extra fields before saving
        return User.objects.create_user(**validated_data)
