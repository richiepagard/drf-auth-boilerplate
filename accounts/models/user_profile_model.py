from django.db import models
from django.utils.translation import gettext_lazy as _

from .user_model import User


class UserProfile(models.Model):
    """
    Represents users' profiles in the system. Users' profile detail.
    A O2O relation with User. Some personal info
    of users handled here to organized the authentication
    and the unnecessary info.

    Attributes:
        user (int, O2O): The owner of the created profile.
        nickname (str): A display name shown in the user interface.
        bio (str): A short description or biography of the user.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("User"),
        help_text=_("User who is the owner of this profile.")
    )
    nickname = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name=_("Nickname")
    )
    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Bio"),
        help_text=_("Short description about the user.")
    )

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("Users Profiles")

    def __str__(self) -> str:
        username = self.user.username
        nickname = self.nickname

        if self.nickname:
            return f"{username} - {nickname}"
        else:
            return f"{username}"
