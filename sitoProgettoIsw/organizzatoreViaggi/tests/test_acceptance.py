from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import ta_log
import ta_travel

driver = webdriver.Firefox()
driver.get("http://localhost:8000")

##Test creazione sito
ta_log.login(driver)
ta_travel.create_travel(driver)
ta_travel.mytravel(driver)
ta_log.logout(driver)

##Test modifica viaggio
ta_log.login(driver)
ta_travel.mytravel(driver)
ta_travel.details_travel(driver)
ta_travel.modify_travel(driver)
ta_travel.form_modify_travel(driver)
ta_travel.details_travel(driver)
ta_travel.modify_travel(driver)
ta_travel.form_create_location(driver)
ta_travel.details_travel(driver)
ta_travel.modify_travel(driver)
ta_travel.form_delete_location(driver)
ta_log.logout(driver)

##Test manda inviti
ta_log.login(driver)
ta_travel.mytravel(driver)
ta_travel.details_travel(driver)
ta_travel.send_invite(driver)
ta_travel.choose_invite(driver)
ta_log.logout(driver)

##Test modifica spese
ta_log.login(driver)
ta_travel.mytravel(driver)
ta_travel.details_travel(driver)
ta_travel.modify_expense(driver)
ta_log.logout(driver)