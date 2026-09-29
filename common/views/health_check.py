from django.db import connections
from django.db.utils import OperationalError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check_dependecy(request) -> Response:
    """
    Health check to checks the dependecies connectivity,
    such as database connection.
    """
    health_status = {
        "status": "healthy",
        "checks": {}
    }

    try:
        # Gets the default database from the database connections
        # and interacting with the database (cursor)
        db_connection = connections["default"]
        db_connection.cursor()

        # If the database interacted and connected, it is healthy
        health_status["checks"]["database"] = "healthy"

    except OperationalError as operationl_error:
        print(f"Database health check failed: {str(operationl_error)}")

        # If raised OperationalError from the database connection
        # the database connection and the application health status
        # are both unhealthy
        health_status["checks"]["database"] = "unhealthy"
        health_status["status"] = "unhealthy"

    # Return appropriate status code
    if health_status.get("status") == "healthy":
        return Response(
            health_status,
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            health_status,
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
