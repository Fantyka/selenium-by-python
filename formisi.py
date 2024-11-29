from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#konfigurasi chrome driver
option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=option)

#Buka halaman web
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
#MENUNGGU HALAMAN WEB
driver.implicitly_wait(10)


driver.find_element(By.XPATH,"//*[@id='userName']").send_keys("fantyka")
time.sleep(5)
driver.find_element(By.ID,"userEmail").send_keys("bintang07@gmail.com")
time.sleep(5)
driver.find_element(By.ID,"currentAddress").send_keys("Jl. duta graha")
time.sleep(5)
driver.find_element(By.ID,"permanentAddress").send_keys("Jl. Wora-Wari")
time.sleep(5)
driver.find_element(By.ID,"submit").click()
time.sleep(5)
