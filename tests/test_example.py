import pytest


def hello(name: str) -> str:
    """A simple greeting.

    Args:
        name (str): Name to greet.
    Returns:
        str: greeting message
    """
    return f"Hello {name}!"


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("J. Doe", "Hello J. Doe!"),
        ("traveler", "Hello traveler!"),
        ("developer", "Hello developer!"),
    ],
)
def test_hello(name, expected):
    """Example test with parametrization."""
    assert hello(name) == expected
