"""
Pytest configuration and fixtures.
"""

import pytest


# Add fixtures here as needed
@pytest.fixture()
def sample_success_value():
    return 42


@pytest.fixture()
def sample_error_value():
    return "error message"
