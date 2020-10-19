import pytest

from api_tests.config_files import config
from api_tests.config_files.environments import ENV


@pytest.fixture()
def switch_app(client_id: str, client_secret: str):
    def switch_app_fixture():
        print("here")
        config.CLIENT_ID = ENV['oauth'][client_id]
        config.CLIENT_SECRET = ENV['oauth'][client_secret]
        config.REDIRECT_URI = "https://example.com/callback"

    return switch_app_fixture
