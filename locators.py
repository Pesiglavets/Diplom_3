from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")

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

class ConstructorPageLocators:
    INGREDIENT_SECTION = (By.CSS_SELECTOR, "[class*='BurgerIngredients_ingredients__1N8v2']")
    INGREDIENT_ITEM = (By.CSS_SELECTOR, "[class*='BurgerIngredient_ingredient__']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "[class*='counter_counter__']")
    CONSTRUCTOR_AREA = (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда (верх)')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

class ConstructorModalLocators:
    MODAL = (By.CSS_SELECTOR, "[class*='Modal_modal__contentBox__sCy8X']")
    MODAL_TITLE = (By.CSS_SELECTOR, "[class*='Modal_modal__title_modified__3Hjkd']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "[class*='Modal_modal__close_modified__3V5XS']")
    INGREDIENT_DETAILS = (By.CSS_SELECTOR, "[class*='Modal_modal__statsList__6cEm5']")
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'Ваш заказ начали готовить')]")

class OrderFeedLocators:
    ORDER_FEED_SECTION = (By.CSS_SELECTOR, "[class*='OrderFeed_orderFeed__']")
    ORDER_CARDS = (By.CSS_SELECTOR, "[class*='OrderHistory_listItem__']")
    ORDER_MODAL = (By.CSS_SELECTOR, "[class*='Modal_orderBox__1xWdi']")
    ORDER_MODAL_OPENED = (By.CSS_SELECTOR, "[class*='Modal_modal_opened__']")  
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, "//div/section[2]/div[1]/button")

class OrderStatsLocators:
    TOTAL_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.CSS_SELECTOR, "[class*='OrderFeed_orderListReady__1YFem']")