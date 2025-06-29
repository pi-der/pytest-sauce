from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver, config):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.get("timeout", 10))

    def click_checkout_button(self):
        # 在购物车页面点击 Checkout
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()

    def fill_checkout_info(self, first_name, last_name, postal_code):
        # 输入收货人信息
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def click_continue(self):
        # 继续到订单确认页
        continue_btn = self.driver.find_element(By.ID, "continue")
        continue_btn.click()

    def click_finish(self):
        # 完成订单
        finish_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        finish_btn.click()

    def is_order_successful(self):
        # 检查订单是否完成
        try:
            success_msg = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
            )
            return "THANK YOU FOR YOUR ORDER" in success_msg.text.upper()
        except:
            return False
