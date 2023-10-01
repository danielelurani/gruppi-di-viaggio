import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

def travel_void(driver):
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
    elem.send_keys(Keys.RETURN)

    time.sleep(3)

def travel_wrong_date(driver):
    elem = driver.find_element(By.NAME, "name")
    elem.clear()
    elem.send_keys("Accettazione2")

    elem = driver.find_element(By.NAME, "destination")
    elem.clear()
    elem.send_keys("Destinazione2")

    elem = driver.find_element(By.NAME, "start_date")
    elem.clear()
    elem.send_keys("2023-04-20")

    elem = driver.find_element(By.NAME, "end_date")
    elem.clear()
    elem.send_keys("2023-01-01")

    elem = driver.find_element(By.NAME, "create_travel")
    elem.send_keys(Keys.RETURN)

    time.sleep(3)

def modify_travel_void(driver):
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/a/button")
    elem.click()

    elem = driver.find_element(By.NAME, "name")
    elem.clear()

    elem = driver.find_element(By.NAME, "destination")
    elem.clear()

    elem = driver.find_element(By.NAME, "start_date")
    elem.clear()

    elem = driver.find_element(By.NAME, "end_date")
    elem.clear()

    elem = driver.find_element(By.NAME, "edit_travel")
    elem.send_keys(Keys.RETURN)

    time.sleep(3)

def add_empty_location(driver):
    elem = driver.find_element(By.NAME, "name_stage")
    elem.clear()

    elem = driver.find_element(By.NAME, "description")
    elem.clear()

    elem = driver.find_element(By.NAME, "date")
    elem.clear()

    elem = driver.find_element(By.NAME, "add_stage")
    elem.click()

    time.sleep(3)

def empty_expense(driver):
    elem = driver.find_element(By.NAME, "aggiungi")
    elem.click()

    time.sleep(3)

def negative_expense(driver):
    elem = driver.find_element(By.NAME, "name")
    elem.clear()
    elem.send_keys("esempio neg")

    elem = driver.find_element(By.NAME, "price")
    elem.clear()
    elem.send_keys("-5")

    elem = driver.find_element(By.NAME, "aggiungi")
    elem.click()

    time.sleep(3)