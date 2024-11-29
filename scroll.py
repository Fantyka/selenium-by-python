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
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)
#MENUNGGU HALAMAN WEB
driver.implicitly_wait(50)


driver.find_element(By.ID,"search").send_keys("jadwal timnas" + Keys.ENTER) 
time.sleep(10)
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
time.sleep(2)

driver.find_element(By.CLASS_NAME,"gs-title").click()
time.sleep(2)
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
time.sleep(5)
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
time.sleep(5)

#TUNGGU SEBENTAR SEBELUM MENUTUP BROWSER
driver.quit()
