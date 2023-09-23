import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def login(driver):
    elem = driver.find_element(By.NAME, "username")
    elem.clear()
    elem.send_keys("admin")

    elem = driver.find_element(By.NAME, "password")
    elem.clear()
    elem.send_keys("admin")

    elem.send_keys(Keys.RETURN)

    time.sleep(1)

def logout(driver):
    elem = driver.find_element(By.XPATH, "//a[2]")
    elem.click()

    time.sleep(1)
