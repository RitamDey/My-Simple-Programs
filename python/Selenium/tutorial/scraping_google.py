import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    # Create a driver instatnce
    driver = webdriver.Firefox()
    # Add WebDriverWait function as an attribute to the driver, so
    # it can be asscessed more easily.
    #This function is used to make the driver wait a certain amount of time
    # (here 5 seconds) for an event to occur.
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, query):
    driver.get("http://www.google.co.in")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
                                (By.NAME, "q")))
        button = driver.wait.until(EC.element_to_be_clickable(
                                (By.NAME, "btnK")))
        box.send_keys(query)
        button.click()
    except TimeoutException:
        print("Box or Button not found at google.co.in")


if __name__ == '__main__':
    driver = init_driver()
    lookup(driver, "Selenium")
    time.sleep(5)
    driver.quit()

