from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def launch_firefox():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")

        # Open Google
        driver.get("https://google.com")

        # Verify Google open successfully
        expected_title = "Google"
        actual_title = driver.title

        if actual_title == expected_title:
            print(f"Google open successfully.Title is: {actual_title}")
        else:
            print(f"Google open failed.Actual Title is: {actual_title} but expected: {expected_title}")

        # close the browser
        driver.close()

    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


launch_firefox()
