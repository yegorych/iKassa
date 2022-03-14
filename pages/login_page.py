import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ikassa_smart.pages.base_page import BasePage
from ikassa_smart.pages.locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Обновить данные СКО и пропустить рекламу")
    def updating_data_and_skipping_ads(self):
        try:
            self.driver.find_element(*LoginPageLocators.UPDATE_DATAS).click() #этот элемент не всегда появляется
        except NoSuchElementException:
            pass
        self.driver.find_element(*LoginPageLocators.ADS_SKIP).click()


    def click_enter_pin_button(self):
        self.driver.find_element(*LoginPageLocators.ENTER_PIN).click()

    def click_enter_user_button(self):
        self.driver.find_element(*LoginPageLocators.ENTER_USER).click()


    @allure.step("Ввод pin от СКО")
    def input_pin_sko(self, pin=None, save_pin=False):
        with allure.step("Ввод пина от СКО"):
            if pin == None:
                pass
            else:
                self.driver.find_element(*LoginPageLocators.SKO_PIN).send_keys(pin)
                if save_pin:
                    self.driver.find_element(*LoginPageLocators.SAVE_PIN).click()
        with allure.step("'Войти' и принять разрешения"):
            self.click_enter_pin_button()
            self.accept_permissions()
            self.click_enter_pin_button()

    @allure.step("Авторизация")
    def log_in_as(self, user_name, password, save_password=False):
        with allure.step("Выбор юзера:"):
            self.driver.find_element(*LoginPageLocators.LIST_USERS).click()
            self.driver.find_element(By.XPATH, f"//android.widget.CheckedTextView[@text='{user_name}']").click()
        with allure.step("Ввод пароля:"):
            self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
            if save_password:
                self.driver.find_element(*LoginPageLocators.SAVE_PIN).click()
        with allure.step("нажатие кнопки 'Войти'"):
            self.click_enter_user_button()


    @allure.step("Проверка наличия сообщения о вводе неверного pin")
    def should_be_incorrect_pin_message(self):
        assert "Неверный пароль" in self.driver.find_element(*LoginPageLocators.INCORRECT_PIN).text, \
            "Сообщение о вводе неправильного пароля отсутствует"

    @allure.step("Проверка наличия сообщения, что нужно ввести pin")
    def should_be_message_that_need_to_enter_password(self):
        assert "Введите пароль" in self.driver.find_element(*LoginPageLocators.NEED_PIN).text, \
            "Сообщение о необходимости ввода pin отсутствует"
