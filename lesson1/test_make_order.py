from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

def test_complete_order():
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
    checkout_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-test='checkout']")))
    checkout_button.click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[data-test='firstName']")))
    first_name = driver.find_element(By.CSS_SELECTOR,"input[data-test='firstName']")
    first_name.send_keys("Petr")
    last_name = driver.find_element(By.CSS_SELECTOR,"input[data-test='lastName']")
    last_name.send_keys("Great")
    zip_code = driver.find_element(By.CSS_SELECTOR, "input[data-test='postalCode']")
    zip_code.send_keys("12345")
    continue_button = driver.find_element(By.CSS_SELECTOR, "input[data-test='continue']")
    continue_button.click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-test='finish']")))
    finish_button = driver.find_element(By.CSS_SELECTOR, "button[data-test='finish']")
    finish_button.click()
    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
    driver.quit()

