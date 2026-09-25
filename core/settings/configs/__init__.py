# Django default conf

from .apps_conf import INSTALLED_APPS
from .middleware_conf import MIDDLEWARE
from .templates_conf import TEMPLATES
from .auth_password_conf import AUTH_PASSWORD_VALIDATORS
from .db_conf import DATABASES

# External apps conf

from .rest_framework_conf import REST_FRAMEWORK
from .jwt_conf import SIMPLE_JWT
from .spectacular_conf import SPECTACULAR_SETTINGS
