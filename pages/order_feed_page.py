import allure
from .base_page import BasePage
from locators import OrderFeedLocators, OrderStatsLocators, ConstructorModalLocators

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()
        self.stats_locators = OrderStatsLocators()
        self.modal_locators = ConstructorModalLocators()

    @allure.step('Кликнуть на заказ в ленте')
    def click_order(self, index=0):
        order_cards = self.find_elements(self.locators.ORDER_CARDS)
        if order_cards and len(order_cards) > index:
            order_cards[index].click()

    @allure.step('Получить общее количество заказов')
    def get_total_orders_count(self):
        try:
            element = self.find_element(self.stats_locators.TOTAL_ORDERS)
            return int(element.text)
        except:
            return 0

    @allure.step('Получить количество заказов за сегодня')
    def get_today_orders_count(self):
        try:
            element = self.find_element(self.stats_locators.TODAY_ORDERS)
            return int(element.text)
        except:
            return 0

    @allure.step('Получить заказы в работе')
    def get_orders_in_progress(self):
        try:
            element = self.find_element(self.stats_locators.ORDERS_IN_PROGRESS)
            return element.text
        except:
            return ""

    @allure.step('Проверить наличие модального окна с деталями заказа')
    def is_order_modal_displayed(self):
        try:
            return self.find_element(self.modal_locators.MODAL).is_displayed()
        except:
            return False

    @allure.step('Закрыть модальное окно заказа')
    def close_order_modal(self):
        self.click_element(self.modal_locators.MODAL_CLOSE_BUTTON)

    @allure.step('Проверить наличие ленты заказов')
    def is_order_feed_section_displayed(self):
        try:
            return self.find_element(self.locators.ORDER_FEED_SECTION).is_displayed()
        except:
            return False