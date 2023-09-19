import os
import time

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from celery import shared_task

from django_project.celery import app


@shared_task
def add(x, y):
    # Example task that can be removed
    print(x + y)


@app.task
def debug_task():
    time.sleep(5)
    return "Debug task slept for 5 second."


@app.task
def celery_beat_debug_task():
    return "Celery beat debug task complete."


@app.task
def send_email_debug_task():
    """
    Sends an email to Django admins
    """

    html_message = render_to_string(
        "emails/email_admins.html",
        {
            "message": "This email was sent successfully.",
        },
    )

    subject = "Debug Admin Email"
    email = EmailMessage(
        subject,
        html_message,
        os.environ.get("DJANGO_EMAIL_HOST_USER", "debug+email@local.dev"),
        [settings.ADMIN_EMAIL],
    )
    email.content_subtype = "html"
    email.send()
