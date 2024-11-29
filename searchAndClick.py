from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#konfigurasi chrome driver
option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=option)

#Buka halaman web
driver.get('https://www.google.com/')
driver.maximize_window()

#menunggu halaman web
driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME,"gLFyf").send_keys("automation" + Keys.ENTER)
driver.find_element(By.PARTIAL_LINK_TEXT,"Automation").click()

#tunggu sebentar sebelum menutup browser
from time import sleep
time.sleep(10)
driver.quit()

