# flake8: noqa

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
from django.conf import settings
from django.db import models
from django.urls import reverse


# Models should always be Capitalized (eg. University, User, Article)
# and singular (eg. University not Universities) since they represents a single object, not multiple objects.
class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(
        verbose_name="some common field name", max_length=20, help_text="Enter field documentation"
    )
    # null is database-related. When a field has null=True it can store a database entry as NULL, meaning no value.

    # blank is validation-related, if blank=True then a form will allow an empty value, whereas if blank=False then a value is required.

    # All 3 are equivalent!
    # full_name = models.CharField(max_length=100)
    # full_name = models.CharField("full name", max_length=100)
    # full_name = models.CharField(verbose_name="full name", max_length=100)

    # Metadata: A good first step is to explicitly name your model too, not just your fields.
    class Meta:
        ordering = [
            "-my_field_name"
        ]  # Ordering is not free; each field to order by is an operation the database must perform.
        verbose_name = "my-model-name"
        verbose_name_plural = "my-model-names"

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName.

        Sets a canonical URL for the model. This is required when using the reverse() function.
        It is also the correct way to refer to a model in your templates rather than hard-coding them.

          <!-- Correct -->
          <a href="{{ object.get_absolute_url }}/">{{ object.full_name }}</a>
        """
        return reverse("model-detail-view", args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    modified_on = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        default=None,
        blank=True,
        editable=False,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_created_by",
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        default=None,
        blank=True,
        editable=False,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_modified_by",
    )

    class Meta:
        abstract = True


class RequestLog(models.Model):
    """
    Request Log
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )
    date = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=3000)
    full_path = models.CharField(max_length=3000)
    execution_time = models.IntegerField(null=True)
    response_code = models.PositiveIntegerField()
    method = models.CharField(max_length=10, null=True)
    remote_address = models.CharField(max_length=20, null=True)
