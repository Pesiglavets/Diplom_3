import allure
from .base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.input_text(self.locators.EMAIL_INPUT, email)

    @allure.step('Ввести пароль')
    def enter_password(self, password):
        self.input_text(self.locators.PASSWORD_INPUT, password)

    @allure.step('Нажать кнопку "Войти"')
    def click_login_button(self):
        self.click_element(self.locators.LOGIN_BUTTON)

    @allure.step('Нажать кнопку "Восстановить пароль"')
    def click_forgot_password_link(self):
        self.click_element(self.locators.FORGOT_PASSWORD_LINK)