from bs4 import BeautifulSoup
import requests
from collections import namedtuple

def collect_pages(max_pages=100):
    url =



def build_job_list(soup):
    job_list = []
    Job = namedtuple('Job', ['title', 'location', 'salary', 'company', 'summary'])
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

def write_to_csv(data):
    file = input("Enter filename: ") + ".csv"
    write_file = open(file, "w")
    columnTitleRow = "Title, Company, Location, Wage, Summary\n"
    write_file.write(columnTitleRow)
    for item in data:
        listing = item.title.replace(",", "") + ", " + \
                  item.company.replace(",", "") + ", " + \
                  item.location.replace(",", "") + ", " + \
                  item.salary.replace(",", "") + ", " + \
                  item.summary.replace(",", "") + "\n"
        write_file.write(listing)


url = requests.get('https://www.indeed.com/jobs?q=%28it+or+Network+or+Engineer+or+System+or+LAN+or+Administrator+or+Computer+or+Technology+or+Analyst%29+-nurse+-counselor+-driver+-burger+-dentist+-gyn+-deli+-therapist+-mechanic+-marine+-restaurant+-hvac+-mechanic+-child+-teacher+-instructor+-part+-hydraulic+-customer+-sales+-physician+-assistant+-car+-hispanic+-dog+-weld+-bartender+-veterinary%2475%2C000&l=Michigan&radius=50&start=10')
page = url.text
soup = BeautifulSoup(page, "html.parser")

jobs = build_job_list(soup)
for job in jobs:
    # print('POSITION \"{}"\ LOCATION \"{}"\ DUTIES \"{}"\ \"{}"\.'.format(job.title, job.location, job.summary, job.company))
    print("POSITION \"{}")
    print("LOCATION \"{}")
    print("SALARY \"{}")
    print("COMPANY \"{}")
    print("DUTIES \"{}")
    print("\n")


write_to_csv(jobs)
