from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import ta_log
import ta_travel
import ta_travel_error
from sitoProgettoIsw.organizzatoreViaggi.models import Travel

##Test registrazione utente
#driver = webdriver.Firefox()
#driver.get("http://localhost:8000/organizzatoreViaggi/signup")
#ta_log.register(driver)

driver = webdriver.Firefox()
driver.get("http://localhost:8000")

##Test creazione viaggio
#ta_log.login(driver)
#ta_travel.create_travel(driver)
#ta_travel.mytravel(driver)
#ta_log.logout(driver)

##Test modifica viaggio
ta_log.login(driver)
ta_travel.mytravel(driver)
ta_travel.details_travel(driver)
#ta_travel.modify_travel(driver)
ta_travel.form_modify_travel(driver)
ta_travel.details_travel(driver)
ta_travel.form_create_location(driver)
ta_travel.details_travel(driver)
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
ta_travel.form_expense(driver)
ta_travel.remove_expense(driver)
ta_log.logout(driver)

##Test commenta
ta_log.login(driver)
ta_travel.mytravel(driver)
ta_travel.details_travel(driver)
ta_travel.write_comment(driver)
ta_log.logout(driver)

##Test creazione viaggio errato
ta_log.login(driver)
ta_travel_error.travel_void(driver)
ta_travel_error.travel_wrong_date(driver)
ta_log.logout(driver)

##Test modifica viaggio errata
ta_log.login(driver)
ta_travel.mytravel(driver)
ta_travel.details_travel(driver)
ta_travel_error.modify_travel_void(driver)
ta_travel_error.add_empty_location(driver)
ta_log.logout(driver)

##Test modifica spese errate
ta_log.login(driver)
ta_travel.mytravel(driver)
ta_travel.details_travel(driver)
ta_travel.modify_expense(driver)
ta_travel_error.empty_expense(driver)
ta_travel_error.negative_expense(driver)
ta_log.logout(driver)
