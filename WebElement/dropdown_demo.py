import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select


def dropdown_select():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
        driver.get("https://the-internet.herokuapp.com/dropdown")
        time.sleep(5)

        # Verify Login open successfully
        expected_title = "The Internet"
        actual_title = driver.title

        if actual_title == expected_title:
            print(f"The internet page open successfully.Title is: {actual_title}")
        else:
            print(f"The internet page open failed.Actual Title is: {actual_title} but expected: {expected_title}")

        # Locate dropdown element
        dropdown_list = driver.find_element(By.CSS_SELECTOR, "select#dropdown")

        # Create reference object of Select by passing dropdown element
        dropdown_options = Select(dropdown_list)

        # Select any dropdown options using Select class methods
        # dropdown_options.select_by_visible_text("Option 1")
        # dropdown_options.select_by_value("2")
        dropdown_options.select_by_index(1)
        time.sleep(4)

        # close the browser
        driver.close()

        print("Test Case Executed Successfully.......")

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


dropdown_select()