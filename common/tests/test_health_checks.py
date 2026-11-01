from unittest.mock import patch

from django.db.utils import OperationalError
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

CONNECTIONS_PATH = "common.views.health_check.connections"


class HealthCheckLivenessTests(APITestCase):
    def setUp(self):
        self.url = reverse("common:health-live")

    def test_returns_200_and_alive_status(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "alive")

    @patch(CONNECTIONS_PATH)
    def test_stays_200_when_database_is_down(self, mock_connections):
        # Simulate a database outage: opening a cursor raises an error
        mock_connections.__getitem__.return_value.cursor.side_effect = (
            OperationalError("Database is down")
        )

        response = self.client.get(self.url)

        # Liveness must NOT depend on the database
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "alive")

    def test_post_is_not_allowed(self):
        response = self.client.post(self.url)

        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )


class HealthCheckReadinessTests(APITestCase):
    def setUp(self):
        self.url = reverse("common:health-ready")

    def test_returns_200_when_database_is_healthy(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "healthy")
        self.assertEqual(response.data["checks"]["database"], "healthy")

    @patch(CONNECTIONS_PATH)
    def test_returns_503_when_database_is_down(self, mock_connections):
        mock_connections.__getitem__.return_value.cursor.side_effect = (
            OperationalError("Database is down")
        )

        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE
        )
        self.assertEqual(response.data["status"], "unhealthy")
        self.assertEqual(response.data["checks"]["database"], "unhealthy")

    def test_post_is_not_allowed(self):
        response = self.client.post(self.url)

        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )
