from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def launch_chrome():
    try:
        driver = webdriver.Chrome()
        print("Launching Chrome Successfully")
    except WebDriverException as e:
        print("Failed to Launch Chrome. Exception: ", str(e))


def launch_safari():
    try:
        driver = webdriver.Safari()
        print("Launching Safari Successfully")
    except WebDriverException as e:
        print("Failed to Launch Safari. Exception: ", str(e))


def launch_firefox():
    try:
        driver = webdriver.Firefox()
        print("Launching Firefox Successfully")
    except WebDriverException as e:
        print("Failed to Launch Firefox. Exception: ", str(e))


def launch_edge():
    try:
        driver = webdriver.Edge()
        print("Launching Edge Successfully")
    except WebDriverException as e:
        print("Failed to Launch Edge. Exception: ", str(e))


launch_chrome()
launch_safari()
launch_firefox()
launch_edge()
