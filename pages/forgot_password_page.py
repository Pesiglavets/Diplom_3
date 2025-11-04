import allure
from .base_page import BasePage
from locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPasswordPageLocators()

    @allure.step('Ввести email для восстановления пароля')
    def enter_email(self, email):
        self.input_text(self.locators.EMAIL_INPUT, email)

    @allure.step('Нажать кнопку "Восстановить"')
    def click_restore_button(self):
        self.click_element(self.locators.RESTORE_BUTTON)