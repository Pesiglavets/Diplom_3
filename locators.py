from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")

class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")

class ResetPasswordPageLocators:
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".input__icon")
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
    PASSWORD_FIELD_CONTAINER  = (By.XPATH, "//div[contains(@class, 'input_type_text')]//label[text()='Пароль']/..")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")

class BlockingLocators:
    MODAL_LOADING = (By.CSS_SELECTOR, "img.Modal_modal__loading__3534A")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")    

class PersonalAccountLocators:
    ORDER_HISTORY_SECTION = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

class OrderHistoryLocators:
    ORDER_CARDS = (By.CSS_SELECTOR, "[class*='OrderHistory_listItem']")