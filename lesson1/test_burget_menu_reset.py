import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
def test_burger_menu_reset(browser):

    browser.get("https://www.saucedemo.com")
    username = browser.find_element(By.CSS_SELECTOR, "input[data-test='username']")
    username.send_keys("standard_user")
    password = browser.find_element(By.CSS_SELECTOR, "input[data-test='password']")
    password.send_keys("secret_sauce")
    login = browser.find_element(By.CSS_SELECTOR, "input[data-test='login-button']")
    login.click()
    bugrer_menu_button = browser.find_element(By.CSS_SELECTOR, "button[id='react-burger-menu-btn']")
    bugrer_menu_button.click()
    reset_button = browser.find_element(By.CSS_SELECTOR, "a[id='reset_sidebar_link']")
    existing_page_source = browser.page_source
    reset_button.click()
    reseted_page_source = browser.page_source
    try:
        assert existing_page_source != reseted_page_source
    except AssertionError:
        raise AssertionError("Reset button does not work")