from bs4 import BeautifulSoup
import requests

html_page = requests.get("https://www.learncpp.com/").text
soup = BeautifulSoup(html_page, "lxml")
for link in soup.findAll('a'):
    print(link.get("href"))