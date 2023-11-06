import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    print("Launching Firefox Successfully")
    driver.implicitly_wait(5)

    yield driver
    driver.quit()


def test_login_orange_valid(driver):
    # Open Orange
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # Verify Login open successfully
    expected_title = "OrangeHRM"
    actual_title = driver.title

    if actual_title == expected_title:
        print(f"Orange Login page open successfully.Title is: {actual_title}")
    else:
        print(f"Orange Login page open failed.Actual Title is: {actual_title} but expected: {expected_title}")

    # Login Action
    # Find username
    username_field = driver.find_element(By.NAME, "username")
    # Type username value
    username_field.send_keys("Admin")
    time.sleep(3)

    # find password
    password_field = driver.find_element(By.NAME, "password")
    # type password value
    password_field.send_keys("admin123")
    time.sleep(3)

    # find login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    # click login button
    login_button.click()
    time.sleep(5)

    # verify login or not
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    actual_url = driver.current_url

    if actual_url == expected_url:
        print(f"Login successfully.")
    else:
        print(f"Login Unsuccessful.Test failed.Actual url is {actual_title}")

    print("Test Case Executed Successfully.......")


def test_login_orange_invalid(driver):
    # Open Orange
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # Verify Login open successfully
    expected_title = "OrangeHRM"
    actual_title = driver.title

    if actual_title == expected_title:
        print(f"Orange Login page open successfully.Title is: {actual_title}")
    else:
        print(f"Orange Login page open failed.Actual Title is: {actual_title} but expected: {expected_title}")

    # Login Action
    # Find username
    username_field = driver.find_element(By.NAME, "username")
    # Type username value
    username_field.send_keys("Admin invalid")
    time.sleep(3)

    # find password
    password_field = driver.find_element(By.NAME, "password")
    # type password value
    password_field.send_keys("admin123")
    time.sleep(3)

    # find login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    # click login button
    login_button.click()
    time.sleep(5)

    # verify login or not
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    actual_url = driver.current_url

    if actual_url == expected_url:
        print(f"Login Unsuccessfully.Test passed")
    else:
        print(f"Login successful.Test failed.Actual url is {actual_title}")

    print("Test Case Executed Successfully.......")
