from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#konfigurasi chrome driver
option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=option)

#Buka halaman web
driver.get("https://www.kompas.com/")
driver.maximize_window()
driver.get_screenshot_as_file("kompas1.png")
time.sleep(1)
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)
driver.get_screenshot_as_file("kompas2.png")
time.sleep(1)
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)
driver.get_screenshot_as_file("kompas3.png")
time.sleep(1)
#MENUNGGU HALAMAN WEB
driver.implicitly_wait(50)



#TUNGGU SEBENTAR SEBELUM MENUTUP BROWSER
driver.quit()
