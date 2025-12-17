from accounts.models import User


def user_response_data(user: User, tokens: dict) -> dict:
    """
    Calling it after 'is_valid()' method in views
    to done the user registration process.

    Returns user information includes user tokens for authentication.
    """
    user_info = {
        "user_id": user.pk,
        "username": user.username,
        "email": user.email,
        "tokens": tokens
    }

    return user_info
