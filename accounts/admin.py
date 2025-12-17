from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import User, UserProfile
from accounts.forms import UserCreationForm, UserChangeForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["username", "email", "is_admin", "is_staff"]
    list_filter = ["is_active", "is_admin", "is_staff"]
    search_fields = ["username", "email"]
    ordering = ["username", "email"]
    filter_horizontal = ["groups", "user_permissions"]
    list_per_page = 30

    fieldsets = (
        [_("Personal Information"),
            {
                "fields": ("username", "email", "password")
            }
        ],
        [_("Permissions"),
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active", "is_admin", "is_staff",
                    "is_superuser", "groups", "user_permissions"
                )
            }
        ],
    )

    add_fieldsets = (
        [_("Personal Information"),
            {
                "fields": ("username", "email", "password1", "password2")
            }
        ],
        [_("Permissions"),
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active", "is_admin", "is_staff", "is_superuser",
                    "groups", "user_permissions"
                )
            }
        ],
    )

    def get_form(self, request, obj=None, **kwargs):
        """
        Customizes the user form based on the user's permissions.

        Checks if the logged-in user is a superuser. If the user is not a superuser, 
        the 'is_superuser' field in the form will be disabled, preventing any changes 
        to this attribute.
        """
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True

        return form


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "nickname"]
    search_fields = ["nickname", "bio"]
    list_per_page = 30
