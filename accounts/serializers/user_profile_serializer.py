from rest_framework import serializers

from accounts.models import UserProfile


class UserProfileRetrieveSerializer(serializers.ModelSerializer):
    """
    User profile retrive serializer to let users see others profile.

    Retrieving user profile with no permission.
    """
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = UserProfile
        fields = ["username", "nickname", "bio"]

    def to_representation(self, instance: UserProfile) -> dict:
        """
        Represents the fallback values, customize them to how shows them in response.
        """
        represenatation = super().to_representation(instance)

        represenatation["nickname"] = represenatation["nickname"] or "Unknown"
        represenatation["bio"] = represenatation["bio"] or "Nothing..."

        return represenatation



class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """
    Updating users profiles.
    """
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = UserProfile
        fields = ["username", "nickname", "bio"]
        read_only_fields = ["username"]

    def update(self, instance: UserProfile, validated_data: dict) -> UserProfile:
        """
        Updates the given instance items (partial update).

        Args:
            instance (user-profile object): The user's profile will updated.
            validated_data (dict): The data sent by client and validated by system.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def to_representation(self, instance: UserProfile) -> dict:
        """
        Represents the fallback values, customize them to how shows them in response.
        """
        representation = super().to_representation(instance)

        representation["nickname"] = representation["nickname"] or "Unknown"
        representation["bio"] = representation["bio"] or "Nothing..."

        return representation
