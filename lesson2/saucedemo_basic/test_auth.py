from selenium.webdriver.common.by import By
from lesson2.saucedemo_basic.data import *
from lesson2.saucedemo_basic.locators import *
import time

def test_login_form(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH,PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH,LOGIN_BUTTON).click()
    time.sleep(2)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"