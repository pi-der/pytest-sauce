from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver, config):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.get("timeout", 10))

    def add_product_to_cart(self, product_name):
        """
        根据商品名称点击“Add to cart”按钮
        """
        xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        add_button.click()

    def is_product_in_cart(self, product_name):
        """
        判断商品是否已添加（按钮变成Remove状态）
        """
        xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[text()='Remove']"
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except:
            return False

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
