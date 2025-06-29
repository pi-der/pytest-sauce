from time import sleep

import pytest
from selenium import webdriver
from utils.config_manager import ConfigLoader
from utils.logger import get_logger


@pytest.fixture(scope="session")
def config():
    return ConfigLoader()

@pytest.fixture(scope="session")
def logger():
    return get_logger()

@pytest.fixture(scope="function")
def driver(config, request):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(config.get("timeout", 10))
    yield driver
    if request.node.rep_call.failed:
        driver.save_screenshot(f"src/test_failed_{request.node.name}.png")
    sleep(3)
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
