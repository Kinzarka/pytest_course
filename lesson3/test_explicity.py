import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest






@pytest.fixture
def firefox_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(firefox_options):
    driver = webdriver.Firefox(options=firefox_options)
    return driver

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait

def test_visible_after_with_explicit_waits(driver, wait):
    driver.get('https://victoretc.github.io/selenium_waits/')
    title = driver.find_element(By.CSS_SELECTOR,"h1")
    assert title.text == "Практика с ожиданиями в Selenium"

    #Дождаться появления кнопки "Начать тестирование"
	#Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
    begin_testing_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[id='startTest']")))
    assert begin_testing_button, "No button appears"

    #Начать тестирование: Кликнуть по кнопке "Начать тестирование".
    begin_testing_button.click()

    #Ввод логина: Ввести "login" в поле для логина.
    login_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='login']")))
    login_input.send_keys("User")

    #Ввод пароля: Ввести "password" в поле для пароля.
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='password']")))
    password_input.send_keys("Password")

    #Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
    agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='agree']")))
    agree_button.click()

    #Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
    register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='register']")))
    register_button.click()

    #Проверка загрузки: Удостовериться, что появился индикатор загрузки.
    loader_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='loader']")))
    assert loader_icon.is_displayed()

    #Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
    success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p[id='successMessage']")))
    assert success_message.text == "Вы успешно зарегистрированы!"





