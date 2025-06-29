import pytest
from utils.logger import get_logger

class BaseTest:
    # 初始化日志记录器
    logger = get_logger()

    @pytest.fixture(autouse=True)
    def init(self, driver, config):
        # 自动注入 driver 和 config 到实例中
        self.driver = driver
        self.config = config
        self.logger.info("初始化 BaseTest 成功")