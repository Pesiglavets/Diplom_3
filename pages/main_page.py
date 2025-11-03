import allure
from .base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step('Нажать кнопку "Войти в аккаунт"')
    def click_login_button(self):
        self.click_element(self.locators.LOGIN_BUTTON)

    @allure.step('Нажать кнопку "Личный кабинет"')
    def click_personal_account_button(self):
        self.click_element(self.locators.PERSONAL_ACCOUNT_BUTTON)

    