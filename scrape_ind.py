from bs4 import BeautifulSoup
import requests
url = requests.get('https://www.indeed.com/jobs?q=%28it+or+Network+or+Engineer+or+System+or+LAN+or+Administrator+or+Computer+or+Technology+or+Analyst%29+-nurse+-counselor+-driver+-burger+-dentist+-gyn+-deli+-therapist+-mechanic+-marine+-restaurant+-hvac+-mechanic+-child+-teacher+-instructor+-part+-hydraulic+-customer+-sales+-physician+-assistant+-car+-hispanic+-dog+-weld+-bartender+%2475%2C000&l=Michigan&radius=50&start=10')
req = url.text
soup = BeautifulSoup(req, "html.parser")
titles = soup.findAll("a", attrs={"data-tn-element": "jobTitle"})
for item in titles:
    print(item["title"])

