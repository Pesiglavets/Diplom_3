import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage

class TestForgotPassword:
    @allure.title("Переход на страницу восстановления пароля")
    def test_navigate_to_forgot_password_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_login_button()

        login_page.wait_for_page_ready()
        login_page.click_forgot_password_link()

        current_url = login_page.get_current_url()
        assert "forgot-password" in current_url

    @allure.title("Восстановление пароля с валидным email")
    def test_password_recovery_with_valid_email(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_login_button()

        login_page.wait_for_page_ready()
        login_page.click_forgot_password_link()

        test_email = "test@testmail.com"
        forgot_password_page.wait_for_page_ready()
        forgot_password_page.enter_email(test_email)
        forgot_password_page.click_restore_button()

        reset_password_page.wait_for_page_ready()
        current_url = reset_password_page.get_current_url()
        assert "reset-password" in current_url

    @allure.title("Активация поля пароля при клике на кнопку показать/скрыть")
    def test_show_hide_password_button_activates_field(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        main_page.go_to_site()
        main_page.wait_for_page_ready()
        main_page.click_login_button()
        
        login_page.wait_for_page_ready()
        login_page.click_forgot_password_link()

        test_email = "test@testmail.com"
        forgot_password_page.wait_for_page_ready()
        forgot_password_page.enter_email(test_email)
        forgot_password_page.click_restore_button()

        reset_password_page.wait_for_page_ready()
        reset_password_page.click_show_password_button()
        is_active = reset_password_page.is_password_field_active()

            
        assert is_active, "Поля пароля не стало активным после клика на кнопку показать/скрыть"