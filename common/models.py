from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    BaseModel usefully for some field usually use in all models,
    e.g. The created_at and updated_at fields are use in all models.

    Args:
        created_at (str, date): The date and time when the record was created.
        updated_at (str, date): The date and time when the record was last updated.
        is_active (bool): A flag indicating whether the record is active.
    """
    created_at = models.DateTimeField(
        db_index=True,
        default=timezone.now,
        verbose_name=_("Created Date")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Last Updated Date")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Activation Status")
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']
        get_latest_by = 'created_at'
