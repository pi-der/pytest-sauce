from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class HomePage:
    def __init__(self, driver, config):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.get("timeout", 10))

    def is_logged_in(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

    def get_product_titles(self):
        return [el.text for el in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
