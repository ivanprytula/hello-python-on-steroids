# flake8: noqa
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


# class MyModelName(models.Model):
#     """A typical class defining a model, derived from the Model class."""

#     # Fields
#     my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
#     # …

#     # Metadata
#     class Meta:
#         ordering = ["-my_field_name"]

#     # Methods
#     def get_absolute_url(self):
#         """Returns the URL to access a particular instance of MyModelName."""
#         return reverse("model-detail-view", args=[str(self.id)])

#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#         return self.my_field_name


class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=140)

    def __str__(self):
        return self.text[:50]
