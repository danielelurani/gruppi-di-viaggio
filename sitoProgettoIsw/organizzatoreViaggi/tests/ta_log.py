import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def register(driver):
    elem = driver.find_element(By.NAME, "username")
    elem.clear()
    elem.send_keys("MrProva")

    elem = driver.find_element(By.NAME, "first_name")
    elem.clear()
    elem.send_keys("Provolo")

    elem = driver.find_element(By.NAME, "last_name")
    elem.clear()
    elem.send_keys("Provoli")

    elem = driver.find_element(By.NAME, "email")
    elem.clear()
    elem.send_keys("prova@mail.it")

    elem = driver.find_element(By.NAME, "password1")
    elem.clear()
    elem.send_keys("banan3Fritte")

    elem = driver.find_element(By.NAME, "password2")
    elem.clear()
    elem.send_keys("banan3Fritte")

    time.sleep(3)

    elem.send_keys(Keys.RETURN)

    time.sleep(3)

def login(driver):
    elem = driver.find_element(By.NAME, "username")
    elem.clear()
    elem.send_keys("MrProva")

    elem = driver.find_element(By.NAME, "password")
    elem.clear()
    elem.send_keys("banan3Fritte")

    elem.send_keys(Keys.RETURN)

    time.sleep(1)

def logout(driver):
    elem = driver.find_element(By.XPATH, "//a[2]")
    elem.click()

    time.sleep(1)
