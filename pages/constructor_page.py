import allure
from .base_page import BasePage
from locators import ConstructorPageLocators, ConstructorModalLocators

class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ConstructorPageLocators()
        self.modal_locators = ConstructorModalLocators()

    @allure.step('Кликнуть на ингредиент')
    def click_ingredient(self, index=0):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and len(ingredients) > index:
            ingredients[index].click()

    @allure.step('Получить счетчик ингредиента')
    def get_ingredient_counter(self, index=0):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and len(ingredients) > index:
            ingredient = ingredients[index]
            try:
                counter = ingredient.find_element(*self.locators.INGREDIENT_COUNTER)
                return int(counter.text)
            except:
                return 0
        return 0

    @allure.step('Перетащить ингредиент в конструктор через JavaScript')
    def drag_ingredient_to_constructor(self, index=0):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        constructor_area = self.find_element(self.locators.CONSTRUCTOR_AREA)
        
        if ingredients and len(ingredients) > index:
            ingredient = ingredients[index]
            self._drag_and_drop_js(ingredient, constructor_area)

    def _drag_and_drop_js(self, source_element, target_element):
        js_script = """
        function simulateDragDrop(source, target) {
            var dragStart = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: new DataTransfer()
            });
            
            var dragEnter = new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: new DataTransfer()
            });
            
            var dragOver = new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: new DataTransfer()
            });
            
            var drop = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: new DataTransfer()
            });
            
            var dragEnd = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: new DataTransfer()
            });
            
            source.dispatchEvent(dragStart);
            target.dispatchEvent(dragEnter);
            target.dispatchEvent(dragOver);
            target.dispatchEvent(drop);
            source.dispatchEvent(dragEnd);
        }
        
        simulateDragDrop(arguments[0], arguments[1]);
        """
        
        self.driver.execute_script(js_script, source_element, target_element)



    @allure.step('Нажать кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click_element(self.locators.ORDER_BUTTON)

    @allure.step('Проверить наличие модального окна с деталями ингредиента')
    def is_ingredient_modal_displayed(self):
        try:
            return self.find_element(self.modal_locators.MODAL).is_displayed()
        except:
            return False

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.click_element(self.modal_locators.MODAL_CLOSE_BUTTON)

    @allure.step('Проверить наличие блока с ингредиентами')
    def is_ingredient_section_displayed(self):
        try:
            return self.find_element(self.locators.INGREDIENT_SECTION).is_displayed()
        except:
            return False
        
    @allure.step('Проверить наличие сообщения о принятии заказа')
    def is_success_message_displayed(self):
        try:
            return self.find_element(self.modal_locators.SUCCESS_MESSAGE).is_displayed()
        except:
            return False