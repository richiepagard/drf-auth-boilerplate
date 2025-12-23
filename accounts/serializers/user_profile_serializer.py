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
