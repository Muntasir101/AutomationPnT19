import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pytest_html_reporter import attach

# Define test data as list of tuples (username, password and expected_title)
test_data = [
    ("Admin", "admin123", "OrangeHRM"),
]


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    print("Launching Firefox Successfully")
    driver.implicitly_wait(5)

    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password, expected_title", test_data)
def test_login_orange(driver, username, password, expected_title):
    # Open Orange
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # Verify Login open successfully
    expect_title = expected_title
    actual_title = driver.title

    if actual_title == expect_title:
        print(f"Orange Login page open successfully.Title is: {actual_title}")

        # add screenshot on report
        screenshot = driver.get_screenshot_as_png()
        attach(data=screenshot)

    else:
        print(f"Orange Login page open failed.Actual Title is: {actual_title} but expected: {expected_title}")

    # Login Action
    # Find username
    username_field = driver.find_element(By.NAME, "username")
    # Type username value
    username_field.send_keys(username)
    time.sleep(3)

    # find password
    password_field = driver.find_element(By.NAME, "password")
    # type password value
    password_field.send_keys(password)
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
        print(f"Login Unsuccessful.")

    print("Test Case Executed Successfully.......")
