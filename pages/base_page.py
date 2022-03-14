from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ikassa_smart.pages.locators import AndroidPermissons



class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def accept_permissions(self):
        self.driver.find_element(*AndroidPermissons.PERMISSIONS).click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=5):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def is_not_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False