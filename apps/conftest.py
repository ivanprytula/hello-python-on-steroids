import pytest
from rest_framework.test import APIClient

from apps.users.models import User
from apps.users.tests.factories import UserFactory

CUSTOMER_NAME = "regular-user"
CUSTOMER_PASSWORD = "customer^Events-@pp"


ADMIN_NAME = "admin-user"
ADMIN_PASSWORD = "events-@pp-@dm1N"


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def events_admin_user(db) -> User:
    return UserFactory(name=ADMIN_NAME, password=ADMIN_PASSWORD, is_staff=True)


@pytest.fixture
def api_client() -> APIClient:
    """
    Purpose: The APIClient is designed to provide a higher-level interface for testing APIs.
    It allows you to make HTTP requests to your API endpoints and perform assertions on the responses.
    Usage: You can create an instance of APIClient and use its methods (e.g., get(), post(), put()
    , patch(), delete()) to make HTTP requests to your API endpoints.
    The APIClient handles sending the request, receiving the response,
    and provides methods for asserting the response status code, content, headers, etc.
    It also supports authentication and session handling.
    """
    return APIClient()


# @pytest.fixture
# def anonymous_api_client(api_client):
#     # No authentication for anonymous user
#     return api_client


@pytest.fixture
def auth_customer_client(api_client, user):
    api_client.login(name=CUSTOMER_NAME, password=CUSTOMER_PASSWORD)
    return api_client


@pytest.fixture
def auth_admin_client(api_client, events_admin_user):
    api_client.login(name=ADMIN_NAME, password=ADMIN_PASSWORD)
    return api_client


@pytest.fixture(autouse=True)
def whitenoise_autorefresh(settings):
    """
    Get rid of whitenoise "No directory at" warning, as it's not helpful when running tests.

    Related:
        - https://github.com/evansd/whitenoise/issues/215
        - https://github.com/evansd/whitenoise/issues/191
        - https://github.com/evansd/whitenoise/commit/4204494d44213f7a51229de8bc224cf6d84c01eb
    """
    settings.WHITENOISE_AUTOREFRESH = True
