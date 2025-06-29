import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.data_loader import load_test_data
from tests.base_test import BaseTest

@pytest.mark.parametrize("data", load_test_data("data.yaml"))
class TestProduct(BaseTest):

    def test_add_product_to_cart(self, data):
        if data["expected"] != "success":
            pytest.skip(f"{data['username']} 登录失败或不可用，跳过加购测试")

        # 登录
        login = LoginPage(self.driver, self.config)
        login.open(self.config.get("base_url"))
        login.login(data["username"], data["password"])

        # 添加商品
        product_page = ProductPage(self.driver, self.config)
        product_page.add_product_to_cart("Sauce Labs Backpack")

        # 验证商品是否添加成功
        assert product_page.is_product_in_cart("Sauce Labs Backpack")

        # 点击购物车
        product_page.go_to_cart()
