import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeed:

    @allure.title("Открытие модального окна с деталями заказа при клике")
    def test_click_order_opens_modal(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_order_feed_button()
        order_feed_page.wait_for_page_ready()
        
        order_feed_page.click_order()
        order_feed_page.wait_for_page_ready()
        
        assert order_feed_page.is_order_modal_displayed()

    @allure.title("Закрытие модального окна заказа по крестику")
    def test_close_order_modal(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_order_feed_button()
        order_feed_page.wait_for_page_ready()
        
        order_feed_page.click_order()
        order_feed_page.wait_for_page_ready()
        order_feed_page.close_order_modal()
        order_feed_page.wait_for_page_ready()
        
        assert not order_feed_page.is_order_modal_displayed()

    @allure.title("Заказы пользователя отображаются в истории и ленте заказов")
    def test_user_orders_in_history_and_feed(self, driver, authenticated_user):
        email, password, name, auth_token = authenticated_user
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_personal_account_button()
        personal_account_page.wait_for_page_ready()
        personal_account_page.go_to_order_history()
        personal_account_page.wait_for_page_ready()
        
        history_has_orders = personal_account_page.are_order_cards_displayed()
        
        main_page.click_order_feed_button()
        order_feed_page.wait_for_page_ready()
        
        feed_has_orders = order_feed_page.are_order_cards_displayed()
        
        assert history_has_orders and feed_has_orders

    @pytest.mark.parametrize("counter_type,method_name", [
        ("total", "get_total_orders_count"),
        ("today", "get_today_orders_count")
    ])
    @allure.title("Счетчик '{counter_type}' увеличивается при создании нового заказа")
    def test_order_counter_increases(self, driver, order_data, api_client, counter_type, method_name):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_order_feed_button()
        order_feed_page.wait_for_page_ready()
        
        get_counter_method = getattr(order_feed_page, method_name)
        initial_count = get_counter_method()
        
        if order_data['ingredient_id']:
            api_client.create_order([order_data['ingredient_id']], order_data['auth_token'])
        
        driver.refresh()
        order_feed_page.wait_for_page_ready()
        
        new_count = get_counter_method()
        
        assert new_count > initial_count


    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, driver, order_data, api_client):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_order_feed_button()
        order_feed_page.wait_for_page_ready()
        
        if order_data['ingredient_id']:
            order_number, is_appeared = order_feed_page.create_order_and_wait_in_progress(
                api_client, 
                [order_data['ingredient_id']], 
                order_data['auth_token'],
                timeout=15
            )
            
            assert is_appeared, f"Order number {order_number} didn't appear in progress orders"
            
            progress_orders = order_feed_page.get_orders_in_progress()
            assert str(order_number) in progress_orders