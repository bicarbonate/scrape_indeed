from bs4 import BeautifulSoup
import requests
from collections import namedtuple


def build_job_list(soup):
    job_list = []
    Job = namedtuple('Job', ['title', 'location', 'summary', 'salary', 'company'])
    for div in soup.find_all(name="div", attrs={"class": "row"}):
        job_title = (div.find(name="a", attrs={"data-tn-element": "jobTitle"}))
        job_location = (div.find(name="span", attrs={"class": "location"}))
        job_summary = (div.find(name="span", attrs={"class": "summary"}))
        job_salary = (div.find(name="span", attrs={"class": "no-wrap"}))
        if job_salary == None:
            job_salary = "Unknown"
        else:
            job_salary = job_salary.text
        job_company = (div.find(name="span", attrs={"class": "company"}))
        job_list.append(Job(job_title["title"],
                            job_location.text.strip(),
                            job_summary.text.strip(),
                            job_company.text.strip(),
                            job_salary.strip()))
    return job_list

url = requests.get('https://www.indeed.com/jobs?q=%28it+or+Network+or+Engineer+or+System+or+LAN+or+Administrator+or+Computer+or+Technology+or+Analyst%29+-nurse+-counselor+-driver+-burger+-dentist+-gyn+-deli+-therapist+-mechanic+-marine+-restaurant+-hvac+-mechanic+-child+-teacher+-instructor+-part+-hydraulic+-customer+-sales+-physician+-assistant+-car+-hispanic+-dog+-weld+-bartender+-veterinary%2475%2C000&l=Michigan&radius=50&start=10')
page = url.text
soup = BeautifulSoup(page, "html.parser")

jobs = build_job_list(soup)
for job in jobs:
    print('POSITION \"{}"\ LOCATION \"{}"\ DUTIES \"{}"\ \"{}"\.'.format(job.title, job.location, job.summary, job.company))

