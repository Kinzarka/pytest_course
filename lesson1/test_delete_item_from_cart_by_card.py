from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

def test_delete_item_from_card():
    driver.get("https://www.saucedemo.com")
    username = driver.find_element(By.CSS_SELECTOR, "input[data-test='username']")
    username.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR, "input[data-test='password']")
    password.send_keys("secret_sauce")
    login = driver.find_element(By.CSS_SELECTOR, "input[data-test='login-button']")
    login.click()
    item_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Sauce Labs Bike Light']")))
    item_link.click()
    add_to_cart_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-bike-light']")))
    add_to_cart_button.click()
    shopping_cart_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='shopping_cart_link']")))
    shopping_cart_button.click()
    link_item_card = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='inventory_item_name']")))
    link_item_card.click()
    remove_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-bike-light']")))
    remove_button.click()
    check_add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-bike-light']")
    assert check_add_to_cart_button.is_displayed()
    driver.quit()
