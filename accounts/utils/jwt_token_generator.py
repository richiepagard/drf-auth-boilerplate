from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User


def get_tokens_for_user(user: User) -> dict:
    """
    Generate access and refresh tokens for a specified user.

    Arguments:
        user (User): A user instance from the 'request.user' or the main model.

    Returns:
        dict: A dictionary that includes refresh and access tokens.
    """
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }
