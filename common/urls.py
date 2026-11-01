from django.urls import path

from common.views import (
    health_check_readiness,
    health_check_liveness
)


app_name = "common"

HEALTH_CHECK_URLS = [
    path("health/live/", health_check_liveness, name="health-live"),
    path("health/ready/", health_check_readiness, name="health-ready"),
]

urlpatterns = HEALTH_CHECK_URLS
