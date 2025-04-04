from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Represent a user in the system, including authentication and profile details.

    Attributes:
        username (str): A unique identifier for authentication.
        email (str): The user's email address, used for communication and  account activation.
        nickname (str, optional): A display name shown in the user interface.
    """

    username = models.CharField(
        max_length=30,
        unique=True,
        verbose_name=_("Username")
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_("Email Address")
    )
    nickname = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name=_("Nickname")
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active")
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name=_("Admin")
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Staff Status")
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]


    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


    def __str__(self) -> str:
        return self.nickname or str(_("Unnamed user!"))

    def save(self, *args, **kwargs):
        if self.username:
            self.username = self.username.strip().lower()
        if self.email:
            self.email = self.email.strip().lower()
        if self.nickname:
            self.nickname = self.nickname.strip().lower()

        if self.is_admin:
            self.is_staff = True    # Ensure all admins have staff privileges

        return super().save(*args, **kwargs)
