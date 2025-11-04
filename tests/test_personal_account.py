import pytest
import allure
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.login_page import LoginPage


class TestPersonalAccount:

    @allure.title("Переход по клику на 'Личный кабинет'")
    def test_navigate_to_personal_account(self, driver, authenticated_user):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        
        main_page.click_personal_account_button()
        personal_account_page.wait_for_page_ready()
        
        current_url = personal_account_page.get_current_url()
        assert "/account/profile" in current_url


    @allure.title("Переход в раздел 'История заказов' по кнопке")
    def test_navigate_to_order_history_by_url(self, driver, authenticated_user):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_personal_account_button()
        personal_account_page.wait_for_page_ready()
        personal_account_page.go_to_order_history()
        personal_account_page.wait_for_page_ready()

        current_url = personal_account_page.get_current_url()
        assert "/account/order-history" in current_url
        assert personal_account_page.are_order_cards_displayed()

    @allure.title("Выход из аккаунта по кнопке")
    def test_logout_redirects_to_login(self, driver, authenticated_user):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        login_page = LoginPage(driver)
        
        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_personal_account_button()
        personal_account_page.wait_for_page_ready()
        personal_account_page.logout()
        personal_account_page.wait_for_page_ready()        
        assert login_page.is_login_button_displayed()
        current_url = login_page.get_current_url()
        assert "/login" in current_url