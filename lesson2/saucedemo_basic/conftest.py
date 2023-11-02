import pytest
from selenium import webdriver
from lesson2.saucedemo_basic.data import *
from lesson2.saucedemo_basic.locators import *
import time
from selenium.webdriver.common.by import By
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver 
    print('\nquit browser...')
    driver.quit()

@pytest.fixture()
def login(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH,PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH,LOGIN_BUTTON).click()
    time.sleep(2)
    yield driver