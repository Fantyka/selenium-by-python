from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.kompas.com/")

alamat = driver.current_url
judul = driver.title
panjangjudul = len(judul)

print("Alamat situs {} dan judul adalah {}, dengan panjang {}".format(alamat,judul,panjangjudul))