"""
Django coding style which provides a recommended ordering for models:
- choices
- database fields
- custom manager attributes
- Meta
- def __str__()
- def save()
- def get_absolute_url()
- custom methods
"""


from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse

from apps.users.managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for the project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField("Name of User", blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField("Email address", unique=True)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
