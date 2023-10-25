from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time
from faker import Faker

fake = Faker()


def login_testcase1():
    try:
        driver = webdriver.Firefox()
        print("launching Browser")

        # apply implicit wait
        driver.implicitly_wait(5)

        # open url
        driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

        # Verify Login open successfully
        expected_title = "Register Account"
        actual_title = driver.title
        if expected_title == actual_title:
            print(f" open successfully {expected_title}")

        else:
            print(f"open failed Because Actual Result is {actual_title} ")

        # Login action

        # find fname
        username_fname = driver.find_element(By.NAME, "firstname")
        username_fname.send_keys(fake.name())
        time.sleep(4)

        # find lname
        username_lname = driver.find_element(By.NAME, "lastname")
        username_lname.send_keys(fake.name())

        # find email
        username_email = driver.find_element(By.NAME, "email")
        username_email.send_keys(fake.email())

        # find phone
        username_phone = driver.find_element(By.NAME, "telephone")
        username_phone.send_keys("012345678")

        # find password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("12345678")

        # find confirm password
        password_confirm = driver.find_element(By.NAME, "confirm")
        password_confirm.send_keys("12345678")

        # find newsletter for yes
        username_newsletter_yes = driver.find_element(By.CSS_SELECTOR,
                                                      "label:nth-of-type(1) > input[name='newsletter']")
        username_newsletter_yes.click()

        # find agree
        username_agree = driver.find_element(By.CSS_SELECTOR, "input[name='agree']")
        username_agree.click()

        # Submit button
        login_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        # click Submit button
        login_button.click()
        time.sleep(5)

        # verify Registration or not
        expected_url = "https://tutorialsninja.com/demo/index.php?route=account/success"
        actual_url = driver.current_url

        if actual_url == expected_url:
            print(f"Registration successfully.")
        else:
            print(f"Registration Unsuccessful.Actual url is {actual_url}")

        # close the browser
        driver.close()

    # if error occured
    except WebDriverException as e:
        print("Error launching firefox", str(e))


login_testcase1()
