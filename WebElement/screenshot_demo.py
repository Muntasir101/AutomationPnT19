import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def screenshot_capture():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
        driver.get("https://google.com")
        time.sleep(5)

        # Generate screenshot
        driver.get_screenshot_as_file("E:\\PnT_Online_19\\Projects\\TestAutomationPnT19\\Screenshots\\google.png")

        # close the browser
        driver.quit()

        print("Test Case Executed Successfully.......")

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


screenshot_capture()
