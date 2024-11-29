from selenium import webdriver
from selenium.webdriver.common.by import By

#konfigurasi chrome driver
option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=option)

#Buka halaman web
driver.get("https://www.techlistic.com/p/selenium-practice-form.html#google_vignette")
driver.maximize_window()
#MENUNGGU HALAMAN WEB
driver.implicitly_wait(10)

driver.find_element(By.ID,"photo").send_keys("C:/Users/user/belajarSelenium/kompas1.png")