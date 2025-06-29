from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, config):
        # 初始化 WebDriver 和配置
        self.driver = driver
        self.wait = WebDriverWait(driver, config.get("timeout", 10))

    def open(self, url):
        # 打开目标 URL 页面
        self.driver.get(url)

    def login(self, username, password):
        # 输入邮箱
        username_input = self.wait.until(
            EC.element_to_be_clickable((By.ID,'user-name'))
        )
        username_input.send_keys(username)

        # 输入密码
        password_input = self.wait.until(
            EC.element_to_be_clickable((By.ID,'password'))
        )
        password_input.send_keys(password)

        # 点击登录按钮
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'login-button'))
        )
        login_button.click()

    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text