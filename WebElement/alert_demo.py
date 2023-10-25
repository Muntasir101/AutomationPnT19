import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def normal_alert():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(5)

        # Verify Login open successfully
        expected_title = "The Internet"
        actual_title = driver.title

        if actual_title == expected_title:
            print(f"Orange Login page open successfully.Title is: {actual_title}")
        else:
            print(f"Orange Login page open failed.Actual Title is: {actual_title} but expected: {expected_title}")

        # click to open alert
        driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(1) > button").click()

        # Verify alert text
        expected_text = "I am a JS Alert"
        actual_text = driver.switch_to.alert.text

        if actual_text == expected_text:
            print("Normal Alert open.")
            driver.switch_to.alert.accept()
            time.sleep(3)
        else:
            print("Normal Alert not open.Test Failed")

        # close the browser
        driver.close()

        print("Test Case Executed Successfully.......")

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


normal_alert()


def confirmation_alert():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(5)

        # Verify Login open successfully
        expected_title = "The Internet"
        actual_title = driver.title

        if actual_title == expected_title:
            print(f"Orange Login page open successfully.Title is: {actual_title}")
        else:
            print(f"Orange Login page open failed.Actual Title is: {actual_title} but expected: {expected_title}")

        # click to open alert
        driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(2) > button").click()

        alert = driver.switch_to.alert
        alert.dismiss()
        # alert.accept()

        time.sleep(3)

        # close the browser
        driver.close()

        print("Test Case Executed Successfully.......")

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


# confirmation_alert()

def prompt_alert():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(5)

        # Verify Login open successfully
        expected_title = "The Internet"
        actual_title = driver.title

        if actual_title == expected_title:
            print(f"The internet page open successfully.Title is: {actual_title}")
        else:
            print(f"The internet page open failed.Actual Title is: {actual_title} but expected: {expected_title}")

        # click to open alert
        driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(3) > button").click()

        driver.switch_to.alert.send_keys("Test Automation")
        driver.switch_to.alert.accept()
        time.sleep(3)

        # close the browser
        driver.close()

        print("Test Case Executed Successfully.......")

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))

# prompt_alert()
