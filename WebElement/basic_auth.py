import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def auth():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
        driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        time.sleep(5)

        # close the browser
        driver.quit()

        print("Test Case Executed Successfully.......")

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


auth()
