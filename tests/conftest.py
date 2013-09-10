import pytest

from app import app


@pytest.fixture
def app():
    return app


@pytest.fixture
def client():
    return app.test_client()
