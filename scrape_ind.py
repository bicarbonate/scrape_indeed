from bs4 import BeautifulSoup
import urllib
import requests
url = requests.get('https://www.indeed.com/jobs?q=%28it+or+Network+or+Engineer+or+System+or+LAN+or+Administrator+or+Computer+or+Technology+or+Analyst%29+-nurse+-counselor+-driver+-burger+-dentist+-gyn+-deli+-therapist+-mechanic+-marine+-restaurant+-hvac+-mechanic+-child+-teacher+-instructor+-part+-hydraulic+-customer+-sales+-physician+-assistant+-car+-hispanic+-dog+-weld+-bartender+%2475%2C000&l=Michigan&radius=50&start=10')
soup = BeautifulSoup(url.text, "html.parser")
titles = soup.find(class_='row result')
print(soup)

#titles_list = titles.find_all()
#for titles in titles_list:
#    print(titles.prettify())
