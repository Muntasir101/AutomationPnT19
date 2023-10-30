import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        # apply explicit wait
        username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))

        # state checking
        username_field_display_status = username_field.is_displayed()
        username_field_enable_status = username_field.is_enabled()

        # Type username value
        if username_field_display_status == True and username_field_enable_status == True:
            username_field.send_keys("Admin")
            time.sleep(3)
        else:
            print(f"Cant type on username filed.Because username field display is{username_field_display_status} and "
                  f"enable status is{username_field_enable_status} ")

        # find password
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))

        # type password value
        # state checking
        password_field_display_status = password_field.is_displayed()
        password_field_enable_status = password_field.is_enabled()

        if password_field_display_status == True and password_field_enable_status == True:
            password_field.send_keys("Admin123")
            time.sleep(3)
        else:
            print(f"Cant type on password filed.Because password field display is{password_field_display_status} and "
                  f"enable status is{password_field_enable_status} ")

        # find login button
        login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))

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


login_testCase1_valid()
