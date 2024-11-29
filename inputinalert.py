from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

#konfigurasi chrome driver
option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=option)

#Buka halaman web
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
#MENUNGGU HALAMAN WEB
driver.implicitly_wait(10)

driver.find_element(By.ID,"promtButton").click()
time.sleep(5)

alert = Alert(driver)
alert.send_keys("Tika")
time.sleep(5)
alert.accept()

