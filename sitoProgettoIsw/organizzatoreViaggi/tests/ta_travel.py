import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.support.select


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
    elem.send_keys(Keys.RETURN)

    time.sleep(3)

def details_travel(driver):
    elem = driver.find_element(By.XPATH, "//a[3]")
    elem.click()

    time.sleep(1)

def modify_travel(driver):
    elem = driver.find_element(By.XPATH, "//a[3]")
    elem.click()

    time.sleep(1)

def form_modify_travel(driver):
    elem = driver.find_element(By.NAME, "name")
    elem.clear()
    elem.send_keys("Modifica")

    elem = driver.find_element(By.NAME, "destination")
    elem.clear()
    elem.send_keys("Modifica")

    elem = driver.find_element(By.NAME, "start_date")
    elem.clear()
    elem.send_keys("2023-01-10")

    elem = driver.find_element(By.NAME, "end_date")
    elem.clear()
    elem.send_keys("2023-04-02")

    elem = driver.find_element(By.NAME, "edit_travel")
    elem.send_keys(Keys.RETURN)

    time.sleep(1)

def form_create_location(driver):
    elem = driver.find_element(By.NAME, "name")
    elem.clear()
    elem.send_keys("Tappa")

    elem = driver.find_element(By.NAME, "description")
    elem.clear()
    elem.send_keys("Descrizizone luogo")

    elem = driver.find_element(By.NAME, "date")
    elem.clear()
    elem.send_keys("2023-02-25")

    time.sleep(1)

def form_delete_location(driver):
    elem = driver.find_element(By.NAME, "remove_stage")
    elem.send_keys(Keys.RETURN)

    time.sleep(1)

def send_invite(driver):
    elem = driver.find_element(By.XPATH, "//a[4]")
    elem.click()

    time.sleep(1)

def choose_invite(driver):
    elem = driver.find_element(By.NAME, "receiver")
    elem.clear()
    elem.send_keys("ESEMPIO EMAIL") ##AGGIUNGI EMAIL ESEMPIO A CUI MANDARE INVITO

    elem = driver.find_element(By.NAME, "travel")
    elem.send_keys("p")

    elem = driver.find_element(By.XPATH, "//a[4]")
    elem.click()

    time.sleep(1)

def modify_expense(driver):
    elem = driver.find_element(By.NAME, "send") ##AGGIUNGI NAME send ALL TASTO MANDA INVITO
    elem.click()

    time.sleep(1)