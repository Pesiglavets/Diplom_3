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
            return self.find_element(self.locators.ORDER_MODAL_OPENED).is_displayed()
        except:
            return False

    @allure.step('Закрыть модальное окно заказа')
    def close_order_modal(self):
        self.click_element(self.locators.ORDER_MODAL_CLOSE_BUTTON)

    @allure.step('Проверить наличие ленты заказов')
    def is_order_feed_section_displayed(self):
        try:
            return self.find_element(self.locators.ORDER_FEED_SECTION).is_displayed()
        except:
            return False
        
    @allure.step('Проверить наличие карточек заказов')
    def are_order_cards_displayed(self):
        try:
            order_cards = self.find_elements(self.locators.ORDER_CARDS)
            return len(order_cards) > 0
        except:
            return False
        
    @allure.step('Дождаться появления номера заказа в разделе "В работе"')
    def wait_for_order_in_progress(self, order_number, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        
        def order_number_appeared(driver):
            progress_orders = self.get_orders_in_progress()
            return str(order_number) in progress_orders
        
        try:
            WebDriverWait(self.driver, timeout).until(
                order_number_appeared,
                f"Order number {order_number} didn't appear in progress orders within {timeout} seconds"
            )
            return True
        except:
            return False

    @allure.step('Создать заказ и дождаться его в разделе "В работе"')
    def create_order_and_wait_in_progress(self, api_client, ingredients, auth_token, timeout=10):
        # Создаем заказ через API
        order_response = api_client.create_order(ingredients, auth_token)
        if order_response.status_code == 200:
            order_number = order_response.json()["order"]["number"]
            # Ждем появления заказа в разделе "В работе"
            is_appeared = self.wait_for_order_in_progress(order_number, timeout)
            return order_number, is_appeared
        return None, False