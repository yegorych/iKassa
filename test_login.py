import allure
import pytest
from ikassa_smart.pages.login_page import LoginPage


@allure.suite('Тестирование авторизации')
@pytest.mark.parametrize("user_name, password", [("Администратор", 1234), ("adm", 1111)])
@allure.description("Успешный вход в систему под заданным юзером")
def test_successful_login(driver, user_name, password):
    page = LoginPage(driver)
    page.updating_data_and_skipping_ads()
    page.input_pin_sko(84216, True)
    page.log_in_as(user_name, password, True)

@allure.suite('Тестирование авторизации')
@allure.description("Невозможно атворизоваться введя неверный pin от СКО")
def test_failed_login_due_to_enter_incorrect_pin(driver):
    page = LoginPage(driver)
    page.updating_data_and_skipping_ads()
    page.input_pin_sko(11111)
    page.should_be_incorrect_pin_message()

@allure.suite('Тестирование авторизации')
@allure.description("Невозможно атворизоваться не вводя pin от СКО")
def test_failed_login_due_to_enter_empty_pin(driver):
    page = LoginPage(driver)
    page.updating_data_and_skipping_ads()
    page.input_pin_sko()
    page.should_be_message_that_need_to_enter_password()









