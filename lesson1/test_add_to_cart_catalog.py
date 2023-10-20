from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()


def test_add_to_cart_catalog():
    driver.get("https://www.saucedemo.com")
    user_name = driver.find_element(By.CSS_SELECTOR, 'input[data-test="username"]')
    user_name.send_keys("standard_user")
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-test="password"]')
    password_input.send_keys("secret_sauce")
    log_button = driver.find_element(By.CSS_SELECTOR, 'input[data-test="login-button"]')
    log_button.click()
    backpack_add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    backpack_add_to_cart_button.click()
    shopping_cart_badge = driver.find_element(By.CSS_SELECTOR,".shopping_cart_badge")
    assert shopping_cart_badge.is_displayed()
    driver.quit()