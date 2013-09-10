import pytest

from app import app as testable_app


@pytest.fixture
def app():
    return testable_app


@pytest.fixture
def client(app):
    return app.test_client()
