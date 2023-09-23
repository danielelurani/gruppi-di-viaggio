import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def mytravel(driver):
    elem = driver.find_element(By.XPATH, "//a[1]")
    elem.click()

    time.sleep(1)

def create_travel(driver):
    elem = driver.find_element(By.NAME, "name")
    elem.clear()
    elem.send_keys("Accettazione")

    elem = driver.find_element(By.NAME, "destination")
    elem.clear()
    elem.send_keys("Destinazione")

    elem = driver.find_element(By.NAME, "start_date")
    elem.clear()
    elem.send_keys("2023-02-20")

    elem = driver.find_element(By.NAME, "end_date")
    elem.clear()
    elem.send_keys("2023-03-01")

    elem = driver.find_element(By.NAME, "create_travel")
    elem.clear()
    elem.send_keys(Keys.RETURN)

    time.sleep(3)