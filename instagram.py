from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#konfigurasi chrome driver
option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=option)

#Buka halaman web
driver.get("https://www.instagram.com/")
driver.maximize_window()

#menunggu halaman web
driver.implicitly_wait(10)

driver.find_element(By.NAME,"username").send_keys("fantykabintang@gmail.com")
time.sleep(5)
driver.find_element(By.NAME,"password").send_keys("Fangemini07$@")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button").click()
time.sleep(5)
