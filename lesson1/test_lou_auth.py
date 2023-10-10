from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()


def test_login_form():
    driver.get("https://www.saucedemo.com/")
    error_text = "Epic sadface: Sorry, this user has been locked out."


    user_name = driver.find_element(By.CSS_SELECTOR, 'input[data-test="username"]')
    user_name.send_keys("locked_out_user")
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-test="password"]')
    password_input.send_keys("secret_sauce")
    login_button = driver.find_element(By.CSS_SELECTOR, 'input[data-test="login-button"]')
    login_button.click()
    try:
        error_message = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(.,'Epic sadface: Sorry, this user has been locked out.')]]")))
        assert error_text in error_message.text
        print("Assertion: Text {} is present on the page.".format(error_text))
    except AssertionError:
        print("Assertion: Text {} is not present on the page.".format(error_text))
    except Exception as e:
        print("An error occurred: {}".format(str(e)))

    driver.quit()
