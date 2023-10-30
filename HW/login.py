from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time


def login_testcase1():
    try:
        driver = webdriver.Firefox()
        print("Launching Browser")

        # open url
        driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

        # Verify Login open successfully
        expected_title = "Account Login"
        actual_title = driver.title
        if expected_title == actual_title:
            print(f"Login page open successfully {expected_title}")

        else:
            print(f"open failed Because Actual Result is {actual_title} ")

        # Login action

        # find email
        username_email = driver.find_element(By.NAME, "email")
        username_email.send_keys("anthonygrimes@example.org")
        # Actual email  anthonygrimes@example.org

        # find password
        username_password = driver.find_element(By.NAME, "password")
        username_password.send_keys("GT_VVjpv^9")  # Actual password  GT_VVjpv^9
        time.sleep(5)

        # Submit login button
        login_button = driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[value='Login']")
        # click Submit button
        login_button.click()
        time.sleep(10)

        # verify Login using text
        expected_error_text = "Warning: No match for E-Mail Address and/or Password."
        actual_error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible").text
        if actual_error_message == expected_error_text:
            print(f"Login Unsuccessfully.Get Expected Error Message.Test Passed :)")
        else:
            print(f"Did not get expected Error Message.Test Failed.Actual Error Message is: {actual_error_message}")

        """
        # verify Login using url
        expected_url = "https://tutorialsninja.com/demo/index.php?route=account/account"
        actual_url = driver.current_url

        if actual_url == expected_url:
            print(f"Login successfully.")
        else:
            print(f"Login Unsuccessful.Test failed.Actual url is {actual_url}")

"""
        # close the browser
        driver.close()
        time.sleep(16)

    # if error occured
    except WebDriverException as e:
        print("Error launching firefox", str(e))


login_testcase1()