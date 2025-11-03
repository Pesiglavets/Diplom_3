import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from api_client import ApiClient

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

@pytest.fixture
def api_client():
    return ApiClient()

@pytest.fixture
def authenticated_user(api_client, driver):
    email, password, name = api_client.register_new_user()
    
    from pages.main_page import MainPage
    from pages.login_page import LoginPage
    
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    
    main_page.go_to_site()
    main_page.wait_for_page_ready()
    main_page.click_login_button()
    
    login_page.wait_for_page_ready()
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()
    
    login_response = api_client.login_user(email, password)
    auth_token = login_response.json()["accessToken"]
    
    ingredients = api_client.get_ingredients()
    if ingredients and len(ingredients) > 0:
        ingredients_ids = [ingredients[0]["_id"]]
        api_client.create_order(ingredients_ids, auth_token)

    yield email, password, name, auth_token
    
    api_client.delete_user(auth_token)