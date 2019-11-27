import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Firefox()

file = open("learncpp_final_urls.txt")
file1 = open("learncpp1.html", "w", encoding='utf-8')
file2 = open("learncpp2.html", "w", encoding='utf-8')
file3 = open("learncpp3.html", "w", encoding='utf-8')
file4 = open("learncpp4.html", "w", encoding='utf-8')
file5 = open("learncpp5.html", "w", encoding='utf-8')

for e, f in enumerate(file):
	if e < 50:
		driver.get(f)
		html = driver.page_source
		soup = BeautifulSoup(html)
		file1.write(str(soup))
		time.sleep(3)
	elif e < 100:
		driver.get(f)
		html = driver.page_source
		soup = BeautifulSoup(html)
		file2.write(str(soup))
		time.sleep(3)
	elif e < 150:
		driver.get(f)
		html = driver.page_source
		soup = BeautifulSoup(html)
		file3.write(str(soup))
		time.sleep(3)
	elif e < 200:
		driver.get(f)
		html = driver.page_source
		soup = BeautifulSoup(html)
		file4.write(str(soup))
		time.sleep(3)
	else:
		driver.get(f)
		html = driver.page_source
		soup = BeautifulSoup(html)
		file5.write(str(soup))
		time.sleep(3)

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
