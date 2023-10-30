import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def mouse_hover():

    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
        driver.get("https://demo.opencart.com/")
        time.sleep(5)

        # Verify Login open successfully
        expected_title = "Your Store"
        actual_title = driver.title

        if actual_title == expected_title:
            print(f"The internet page open successfully.Title is: {actual_title}")
        else:
            print(f"The internet page open failed.Actual Title is: {actual_title} but expected: {expected_title}")

        mouse_action = ActionChains(driver)

        desktop = driver.find_element(By.LINK_TEXT, "Desktops")

        mouse_action.move_to_element(desktop).perform()
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "Mac (1)").click()

        print("Title: ", driver.title)

        # close the browser
        driver.quit()

        print("Test Case Executed Successfully.......")

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


mouse_hover()