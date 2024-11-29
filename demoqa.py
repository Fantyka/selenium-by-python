from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#KONFIGURASI CHROME DRIVER
option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=option)

#BUKA HALAMAN WEB
driver.get('https://demoqa.com/select-menu')
driver.maximize_window()

#MENUNGGU HALAMAN WEB
driver.implicitly_wait(10)

pilih = Select (driver.find_element(By.ID,"oldSelectMenu"))
pilih.select_by_visible_text('Yellow')


#TUNGGU SEBENTAR SEBELUM MENUTUP BROWSER
from time import sleep
time.sleep(10)
driver.quit()