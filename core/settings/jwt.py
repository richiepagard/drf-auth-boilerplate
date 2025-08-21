from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    # When set to True, A new refresh token will be returned along with the new access token.
    # This helps in maintaining a valid refresh token and improves security by limiting the lifetime of each refresh token.
    'ROTATE_REFRESH_TOKENS': True,
    # When set to True, old refresh tokens are blacklisted after they are rotated.
    # This prevents the use of a previous refresh token once a new one has been issued, enhancing security.
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',)
}
