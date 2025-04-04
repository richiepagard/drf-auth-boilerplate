from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username, email, nickname=None, password=None):
        if not username:
            raise ValueError(_("User must has a username."))
        if not email:
            raise ValueError(_("User mush has an email address."))
        
        user = self.model(
            username=username,
            # Normalize email to prevent inconsistancies that could lead to `unkind` attacks,
            # where different variations of an email might bypass security checks.
            email=self.normalize_email(email),
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, nickname=None, password=None):
        user = self.create_user(
            username=username,
            email=email,
            nickname=nickname,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
