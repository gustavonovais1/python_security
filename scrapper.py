from bs4 import BeautifulSoup
import requests

site = requests.get('https://web.whatsapp.com/').content

soup = BeautifulSoup(site, 'html.parser')

#print(soup.prettify())

browser = soup.find("h1", class_="landing-title browsers-title")

print(browser.string)

print(soup.title.string)

print(soup.a)