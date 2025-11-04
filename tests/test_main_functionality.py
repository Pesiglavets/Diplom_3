import pytest
import allure
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage

class TestMainFunctionality:
    
    @allure.title("Переход по клику на 'Конструктор'")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_constructor_button()
        constructor_page.wait_for_page_ready()
        assert constructor_page.is_ingredient_section_displayed()
        current_url = constructor_page.get_current_url()
        assert current_url == "https://stellarburgers.education-services.ru/"

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_order_feed_button()
        order_feed_page.wait_for_page_ready()
        assert order_feed_page.is_order_feed_section_displayed()
        current_url = order_feed_page.get_current_url()
        assert "/feed" in current_url

    @allure.title("Открытие модального окна с деталями ингредиента")
    def test_ingredient_modal_opening(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        
        constructor_page.click_ingredient()
        constructor_page.wait_for_page_ready()
        
        assert constructor_page.is_ingredient_modal_displayed()

    @allure.title("Закрытие модального окна ингредиента по крестику")
    def test_ingredient_modal_closing(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        
        constructor_page.click_ingredient()
        constructor_page.wait_for_page_ready()
        constructor_page.close_modal()
        constructor_page.wait_for_page_ready()
        
        assert not constructor_page.is_ingredient_modal_displayed()

    @pytest.mark.smoke
    @allure.title("Увеличение каунтера ингредиента при добавлении в заказ")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        
        initial_counter = constructor_page.get_ingredient_counter()
        constructor_page.drag_ingredient_to_constructor()
        constructor_page.wait_for_page_ready()
        
        new_counter = constructor_page.get_ingredient_counter()
        assert new_counter > initial_counter

    @pytest.mark.smoke
    @allure.title("Оформление заказа залогиненным пользователем")
    def test_authenticated_user_can_create_order(self, driver, authenticated_user):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        
        constructor_page.drag_ingredient_to_constructor()
        constructor_page.wait_for_page_ready()
        constructor_page.click_order_button()
        constructor_page.wait_for_page_ready()
        
        assert constructor_page.is_ingredient_modal_displayed()
        assert constructor_page.is_success_message_displayed()