from selenium import webdriver
import time

#konfigurasi chrome driver
option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
driver1 = webdriver.Chrome(options=option)
driver2 = webdriver.Chrome(options=option)
driver3 = webdriver.Chrome(options=option)

#Buka halaman web
driver1.get('https://www.google.com/')
driver1.maximize_window()

driver2.get('https://premiereclinic.id/locations/bekasi')
driver2.maximize_window()

driver3.get('https://thinkjubilee.com/about/')
driver3.maximize_window()


#MENUNGGU HALAMAN WEB
driver1.implicitly_wait(10)
driver2.implicitly_wait(10)
driver3.implicitly_wait(10)

#TUNGGU SEBENTAR SEBELUM MENUTUP BROWSER
from time import sleep
time.sleep(10)
driver1.quit()
driver2.quit()
driver3.quit()
