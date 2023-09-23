from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import ta_log
import ta_travel

driver = webdriver.Firefox()
driver.get("http://localhost:8000")

ta_log.login(driver)
ta_travel.create_travel(driver)
ta_travel.mytravel(driver)
ta_log.logout(driver)