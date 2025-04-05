from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("Passsword"),
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'nickname']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add placeholder for fields
        self.fields['username'].widget.attrs = {'placeholder': _('Username')}  
        self.fields['email'].widget.attrs = {'placeholder': _('Email address; someone@example.com, etc.')}
        self.fields['nickname'].widget.attrs = {'placeholder': _('Nickname')}

    def clean_password2(self):
        """
        Validate that the two password fields match.

        Compared the password entered in `password1` and `password2` fields.
        If the passwords don't match, raises a validation error.
        But if they match, returns the cleaned `password2` field.
        """
        cleaned_data = self.cleaned_data
        pass1 = cleaned_data['password1']
        pass2 = cleaned_data['password2']

        if pass1 and pass2 and pass2 != pass1:
            raise ValidationError("Passwords don't match!")
        
        return cleaned_data['password2']
    
    def save(self, commit=True):
        """
        Saves the user instance with the hashed password.

        The method overrides the default save behavior to hash the user's password
        before saving the instance to the databse. If `commit` is True,
        the user instance will be saved to the database. If False,
        the instance won't be saved to the database.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text=_(
            "You can change this password with <a href=\"../password/\">this form</a>"
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'nickname', 'password', 'is_active', 'is_admin', 'is_staff']
