import allure
from .base_page import BasePage
from locators import PersonalAccountLocators, OrderHistoryLocators


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PersonalAccountLocators()
        self.order_history_locators = OrderHistoryLocators()

    @allure.step('Перейти в раздел "История заказов"')
    def go_to_order_history(self):
        self.click_element(self.locators.ORDER_HISTORY_SECTION)

    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.click_element(self.locators.LOGOUT_BUTTON)

    @allure.step('Проверить наличие карточек заказов')
    def are_order_cards_displayed(self):
        try:
            order_cards = self.find_elements(self.order_history_locators.ORDER_CARDS)
            return len(order_cards) > 0
        except:
            return False