from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

def test_check_filter_low_to_high():
    driver.get("https://www.saucedemo.com")
    username = driver.find_element(By.CSS_SELECTOR, "input[data-test='username']")
    username.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR, "input[data-test='password']")
    password.send_keys("secret_sauce")
    login = driver.find_element(By.CSS_SELECTOR, "input[data-test='login-button']")
    login.click()
    goods_list = driver.find_elements(By.CSS_SELECTOR, "div[class='inventory_item']")
    initial_positions = [data.text for data in backpack_data]
    select_menu = driver.find_element(By.CSS_SELECTOR, "select[data-test='product_sort_container']")
    select_menu.click()
    low_high = driver.find_element(By.CSS_SELECTOR, "option[value='lohi']")
    low_high.click()
    new_positions = [data.text for data in goods_list]
    assert initial_positions[0] != new_positions[1]
    driver.quit()



