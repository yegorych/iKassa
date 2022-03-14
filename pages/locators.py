from selenium.webdriver.common.by import By


class LoginPageLocators():
    UPDATE_DATAS = (By.ID, "by.imlab.pks.client.ui:id/ok_btn")
    ADS_SKIP = (By.ID, "by.imlab.pks.client.ui:id/openMain")
    SKO_PIN = (By.ID, "by.imlab.pks.client.ui:id/pin_field")
    SAVE_PIN = (By.ID, "by.imlab.pks.client.ui:id/remember_pin_checkbox")
    ENTER_PIN = (By.ID, "by.imlab.pks.client.ui:id/enter_pin_button")
    ENTER_USER = (By.ID, "by.imlab.pks.client.ui:id/enter_user_button")
    LIST_USERS = (By.ID, "by.imlab.pks.client.ui:id/imageView16")
    PASSWORD = (By.ID, "by.imlab.pks.client.ui:id/user_name_password_field")
    INCORRECT_PIN = (By.ID, "by.imlab.pks.client.ui:id/message")
    NEED_PIN = (By.ID, "android:id/message")

class AndroidPermissons():
    PERMISSIONS = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
