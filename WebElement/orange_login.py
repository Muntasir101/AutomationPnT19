import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def login_testCase1_valid():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
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

        # close the browser
        driver.close()

        print("Test Case Executed Successfully.......")

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


def login_testCase2_invalid():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
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

        # Clear username
        username_field.clear()

        # Type username value
        username_field.send_keys("Admin invalid")
        time.sleep(3)

        # find password
        password_field = driver.find_element(By.NAME, "password")

        password_field.clear()

        # type password value
        password_field.send_keys("admin1231212")
        time.sleep(3)

        # find login button
        login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
        # click login button
        login_button.click()
        time.sleep(5)

        # verify login or not using url
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        actual_url = driver.current_url

        if actual_url == expected_url:
            print(f"Login Unsuccessfully.Get Expected URL.Test passed.")
        else:
            print(f"Login successful.Test failed.Actual url is {actual_url}")

        # close the browser
        driver.close()

        print("Test Case Executed Successfully.......")

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


def login_testCase3_invalid():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
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
        password_field.send_keys("admin1231212")
        time.sleep(3)

        # find login button
        login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
        # click login button
        login_button.click()
        time.sleep(5)

        # verify login or not using error message
        expected_error_message = "Invalid credentials"
        actual_error_message = driver.find_element(By.CSS_SELECTOR, ".oxd-alert-content-text").text

        if expected_error_message == actual_error_message:
            print(f"Login Unsuccessfully.Get Expected Error Message.Test Passed.")
        else:
            print(f"Did not get expected Error Message.Test Failed.Actual Error Message is: {actual_title}")

        # close the browser
        driver.close()

        print("Test Case Executed Successfully.......")

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


login_testCase1_valid()
login_testCase2_invalid()
login_testCase3_invalid()
