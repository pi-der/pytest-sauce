import pytest
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from utils.data_loader import load_test_data


@pytest.mark.parametrize("data", load_test_data("data.yaml"))
def test_checkout_success(driver, config, data):
    # 如果不是成功用户或 checkout 数据为空，跳过测试
    if data["expected"] != "success" or not data.get("checkout"):
        pytest.skip(f"{data['username']} 不符合结账条件，跳过")

    # 登录页面
    login = LoginPage(driver, config)
    login.open(config.get("base_url"))
    login.login(data["username"], data["password"])

    # 商品页面 - 添加商品
    product_page = ProductPage(driver, config)
    product_page.add_product_to_cart("Sauce Labs Backpack")
    assert product_page.is_product_in_cart("Sauce Labs Backpack")
    product_page.go_to_cart()

    # 结账页面 - 填写信息并提交
    checkout_page = CheckoutPage(driver, config)
    checkout_page.click_checkout_button()

    info = data["checkout"]
    checkout_page.fill_checkout_info(info["first_name"], info["last_name"], info["postal_code"])
    checkout_page.click_continue()

    try:
        checkout_page.click_finish()
        assert checkout_page.is_order_successful()
    except TimeoutException:
        if data["username"] == "problem_user":
            pytest.xfail("problem_user: 页面 finish 按钮加载异常")
        raise
    except AssertionError:
        if data["username"] == "error_user":
            pytest.xfail("error_user: 结算页面未显示成功提示")
        raise
