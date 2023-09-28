import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

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
    driver.get("http://localhost:8000/organizzatoreViaggi/detailsTravel/29/")

    time.sleep(3)

def modify_travel(driver):
    driver.get("http://localhost:8000/organizzatoreViaggi/changeItinerary/29/")

    time.sleep(3)

def form_modify_travel(driver):
    driver.get("http://localhost:8000/organizzatoreViaggi/changeItinerary/29/")

    time.sleep(3)

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

    time.sleep(3)

def form_create_location(driver):
    driver.get('http://localhost:8000/organizzatoreViaggi/changeItinerary/29/')

    elem = driver.find_element(By.NAME, "name_stage")
    elem.clear()
    elem.send_keys("Tappa")

    elem = driver.find_element(By.NAME, "description")
    elem.clear()
    elem.send_keys("Descrizizone luogo")

    elem = driver.find_element(By.NAME, "date")
    elem.clear()
    elem.send_keys("2023-02-25")

    elem = driver.find_element(By.NAME, "add_stage")
    elem.click()

    time.sleep(3)

def form_delete_location(driver):
    driver.get('http://localhost:8000/organizzatoreViaggi/changeItinerary/29/')

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
    elem.send_keys("Ac")

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