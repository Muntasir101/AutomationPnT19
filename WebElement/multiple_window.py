import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def switch_window():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(5)

        # Verify Login open successfully
        expected_title = "The Internet"
        actual_title = driver.title

        if actual_title == expected_title:
            print(f"The internet page open successfully.Title is: {actual_title}")
        else:
            print(f"The internet page open failed.Actual Title is: {actual_title} but expected: {expected_title}")

        parent_window_id = driver.current_window_handle

        driver.find_element(By.LINK_TEXT, "Click Here").click()

        all_window_ids = driver.window_handles

        # switch to child window
        for child_window_id in all_window_ids:
            if child_window_id not in parent_window_id:
                driver.switch_to.window(child_window_id)
                driver.get("https://google.com")
                time.sleep(5)

        # switch to parent window
        for child_window_id in all_window_ids:
            if child_window_id not in parent_window_id:
                driver.switch_to.window(parent_window_id)
                driver.get("https://apple.com")
                time.sleep(5)

        # close the browser
        driver.quit()

        print("Test Case Executed Successfully.......")

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


switch_window()
