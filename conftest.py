import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class BrowserFactory:
    @staticmethod
    def get_driver(browser_name: str):
        if browser_name == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--start-fullscreen")
            return webdriver.Chrome(options=chrome_options)
        elif browser_name == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--start-fullscreen")
            return webdriver.Firefox(options=firefox_options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = BrowserFactory.get_driver(request.param)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def standard_password():
    return "StandardPassword123"

@pytest.fixture
def generate_email():
    number = random.randint(10000, 99999)
    random_string = ''.join(random.choices(string.ascii_lowercase, k=6))
    new_email = f'test_mail{random_string}_{number}@gmail.com'
    return new_email