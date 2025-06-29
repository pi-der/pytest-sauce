import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.data_loader import load_test_data
from tests.base_test import BaseTest

@pytest.mark.parametrize("data", load_test_data("data.yaml"))
class TestLogin(BaseTest):

    def test_login(self, data):
        page = LoginPage(self.driver, self.config)
        page.open(self.config.get("base_url"))
        page.login(data["username"], data["password"])

        if data["expected"] == "success":
            assert HomePage(self.driver, self.config).is_logged_in()
        elif data["expected"] == "locked":
            assert "locked out" in page.get_error_message().lower()
        else:
            assert "epic sadface" in page.get_error_message().lower()
