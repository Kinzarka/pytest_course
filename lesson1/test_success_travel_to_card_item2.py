from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

def test_succes_travel_to_card_item2():
    driver.get("https://www.saucedemo.com")
    username = driver.find_element(By.CSS_SELECTOR, "input[data-test='username']")
    username.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR, "input[data-test='password']")
    password.send_keys("secret_sauce")
    login = driver.find_element(By.CSS_SELECTOR, "input[data-test='login-button']")
    login.click()
    item_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()[contains(.,'Sauce Labs Backpack')]]")))
    item_link.click()
    assert driver.current_url == ("https://www.saucedemo.com/inventory-item.html?id=4")
    driver.quit()
