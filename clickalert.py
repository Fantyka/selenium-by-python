from selenium import webdriver
from selenium.webdriver.common.by import By
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

driver.find_element(By.ID,"alertButton").click()
time.sleep(10)
alert = Alert(driver)
alert.accept()

