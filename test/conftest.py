import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome", help="my option: chrome or firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    browser_name = request.config.getoption("--browsername")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            service=Service("/Users/vamshi/Downloads/drivers/chromedriver_mac_arm64/chromedriver"), options=opt)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service("/Users/vamshi/Downloads/drivers/geckodriver-v0.32.2-macos-aarch64"
                                                   "/geckodriver"), options=opt)
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # driver.close()
    print("completed!!!!")
