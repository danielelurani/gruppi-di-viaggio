import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def mytravel(driver):
    elem = driver.find_element(By.XPATH, "//a[1]")
    elem.click()

    time.sleep(1)

def create_travel(driver):
    elem = driver.find_element(By.NAME, "name")
    elem.clear()
    elem.send_keys("AAAAA")

    elem = driver.find_element(By.NAME, "destination")
    elem.clear()
    elem.send_keys("BBBBB")

    elem = driver.find_element(By.NAME, "start_date")
    elem.clear()
    elem.send_keys("2023-02-20")

    elem = driver.find_element(By.NAME, "end_date")
    elem.clear()
    elem.send_keys("2023-03-01")

    elem = driver.find_element(By.NAME, "create_travel")
    elem.send_keys(Keys.RETURN)

    time.sleep(3)

def details_travel(driver, trip_id):
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/div[6]/a/p")
    elem.click()

    time.sleep(3)

def form_modify_travel(driver, trip_id):
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/a/button")
    elem.click()

    elem = driver.find_element(By.NAME, "name")
    elem.clear()
    elem.send_keys("AAACC")

    elem = driver.find_element(By.NAME, "destination")
    elem.clear()
    elem.send_keys("BBBDD")

    elem = driver.find_element(By.NAME, "start_date")
    elem.clear()
    elem.send_keys("2023-01-09")

    elem = driver.find_element(By.NAME, "end_date")
    elem.clear()
    elem.send_keys("2023-04-02")

    elem = driver.find_element(By.NAME, "edit_travel")
    elem.send_keys(Keys.RETURN)

    time.sleep(3)

def form_create_location(driver, trip_id):
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/a/button")
    elem.click()

    elem = driver.find_element(By.NAME, "name_stage")
    elem.clear()
    elem.send_keys("Tappa prova")

    elem = driver.find_element(By.NAME, "description")
    elem.clear()
    elem.send_keys("Descrizizone luogo")

    elem = driver.find_element(By.NAME, "date")
    elem.clear()
    elem.send_keys("2023-02-25")

    elem = driver.find_element(By.NAME, "add_stage")
    elem.click()

    time.sleep(3)

def form_delete_location(driver, trip_id):
    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/a/button")
    elem.click()

    elem = driver.find_element(By.NAME, "remove_stage")
    elem.send_keys(Keys.RETURN)

    time.sleep(3)

def send_invite(driver):
    driver.get('http://localhost:8000/organizzatoreViaggi/invite')

    time.sleep(3)

def choose_invite(driver):
    elem = driver.find_element(By.NAME, "receiver")
    elem.clear()
    elem.send_keys("daniele@tiscali.it")

    elem = driver.find_element(By.NAME, "travel")
    elem.send_keys("CCC")

    elem = driver.find_element(By.NAME, "send")
    elem.click()

    elem = driver.find_element(By.XPATH, "//a[1]")
    elem.click()

    time.sleep(3)

def modify_expense(driver):
    elem = driver.find_element(By.NAME, "spese")
    elem.click()

    time.sleep(3)

def form_expense(driver):
    elem = driver.find_element(By.NAME, "name")
    elem.clear()
    elem.send_keys("esempio")

    elem = driver.find_element(By.NAME, "price")
    elem.clear()
    elem.send_keys("10.5")

    elem = driver.find_element(By.NAME, "aggiungi")
    elem.click()

    time.sleep(3)

def remove_expense(driver):
    elem = driver.find_element(By.NAME, "remove")
    elem.click()

    time.sleep(3)

def write_comment(driver):
    elem = driver.find_element(By.ID, "id_content")
    elem.clear()
    elem.send_keys("Commento mandato dal test")

    elem = driver.find_element(By.NAME, "commenta")
    elem.click()

    time.sleep(3)