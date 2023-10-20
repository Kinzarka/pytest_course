from selenium import webdriver
from selenium.webdriver.common.by import By

def test_burger_menu():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com")
    username = driver.find_element(By.CSS_SELECTOR, "input[data-test='username']")
    username.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR, "input[data-test='password']")
    password.send_keys("secret_sauce")
    login = driver.find_element(By.CSS_SELECTOR, "input[data-test='login-button']")
    login.click()
    bugrer_menu_button = driver.find_element(By.CSS_SELECTOR, "button[id='react-burger-menu-btn']")
    bugrer_menu_button.click()
    logout_button = driver.find_element(By.CSS_SELECTOR, "a[id='logout_sidebar_link']")
    logout_button.click()
    assert driver.current_url == "https://www.saucedemo.com/"
    driver.quit()
