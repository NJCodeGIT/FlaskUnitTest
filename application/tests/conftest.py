import pytest
from application import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app(True)
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
