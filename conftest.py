import os
import pytest
import allure
from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "platformVersion": "7.1.1",
    "noReset": False,
    "real_mobile" : "true",
    #"fullReset": False,  # start app with saved data
    #"ignoreHiddenApiPolicyError": True,
    "appPackage": "by.imlab.pks.client.ui",
    "appActivity": "by.imlab.pks.client.ui.ui.activity.main.MainActivity",
    "deviceName": "192.168.100.52:5555"
}

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'driver' in item.fixturenames:
                    driver = item.funcargs['driver']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f'Fail to take screen-shot: {e}')

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

