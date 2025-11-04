import allure
from .base_page import BasePage
from locators import ResetPasswordPageLocators

class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ResetPasswordPageLocators()

    @allure.step('Нажать кнопку показать/скрыть пароль')
    def click_show_password_button(self):
        self.click_element(self.locators.SHOW_PASSWORD_BUTTON)   
   
    @allure.step('Проверить, что поле активно')
    def is_password_field_active(self):
        password_container = self.find_element(self.locators.PASSWORD_FIELD_CONTAINER)
        return "input_status_active" in password_container.get_attribute("class")
    
    @allure.step('Ввести новый пароль')
    def enter_new_password(self, password):
        self.input_text(self.locators.PASSWORD_INPUT_FIELD, password)