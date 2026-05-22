from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Chrome()


def test_input():

    driver.get("https://the-internet.herokuapp.com/login")

    user_input = driver.find_element(By.ID, "username")
    pass_input = driver.find_element(By.ID, "password")

    user_input.send_keys("tomsmith")
    pass_input.send_keys("PasswordSecret!")

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button.radius")
    submit_btn.click()

    flash_message = driver.find_element(By.ID, "flash")

    assert "Your password is invalid!" in flash_message.text

    driver.quit()
  
def test_invalid_password():

    driver.get("https://the-internet.herokuapp.com/login")

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("tomsmith")
    password_input.send_keys("PasswordSecret!")

    login_btn = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_btn.click()

    notif = driver.find_element(By.ID, "flash")

    assert "Your password is invalid!" in notif.text

    driver.quit()