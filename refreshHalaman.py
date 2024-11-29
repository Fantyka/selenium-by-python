from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.kompas.com/")
time.sleep(5)
driver.refresh()
driver.get("https://www.selenium.dev/")
time.sleep(10)
driver.quit()