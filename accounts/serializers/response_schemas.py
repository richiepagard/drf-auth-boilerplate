from drf_spectacular.utils import inline_serializer
from rest_framework import serializers


auth_response  = inline_serializer(
    name="AuthResponse",
    fields={
        "user_id": serializers.IntegerField(),
        "username": serializers.CharField(),
        "email": serializers.EmailField(),
        "tokens": inline_serializer(
            name="UserTokens",
            fields={
                "refresh": serializers.CharField(),
                "access": serializers.CharField(),
            },
        ),
    },
)
