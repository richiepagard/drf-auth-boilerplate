"""
Test the URLs of the accounts app, resolve and others.
Just URLs and how they resolved, work, and how kwargs in the URLs
get a parameter.
"""
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from accounts.views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView
)


class TestUrlsResolved(SimpleTestCase):
    """
    Test if URLs resolved properly.

    URLs:
        accounts-register: User registration URL, test it resolves or not.
        accounts-login: User login URL, test it resolves or not.
        accounts-logout: User logout URL, test it resolves or not.
    """
    def setUp(self):
        self.user_register_url = reverse("accounts:user-register")
        self.user_login_url = reverse("accounts:user-login")
        self.user_logout_url = reverse("accounts:user-logout")

    def test_user_register_url_resolve(self):
        self.assertEqual(resolve(self.user_register_url).func.view_class, UserRegisterView)

    def test_user_login_url_resolve(self):
        self.assertEqual(resolve(self.user_login_url).func.view_class, UserLoginView)

    def test_user_logout_url(self):
        self.assertEqual(resolve(self.user_logout_url).func.view_class, UserLogoutView)
