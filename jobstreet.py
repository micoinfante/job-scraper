import bs4
from bs4 import BeautifulSoup
import requests


class Jobstreet(object):
	
	def __init__(self, job_title, company_name, summary, salary, keywords):
		self.job_title = job_title
		self.company_name = company_name
		self.location = location
		self.summary = summary
		self.salary = salary
		self.keywords = keywords	
		self.URL = 'https://www.jobstreet.com.ph/en/job-search/job-vacancy.php?key='+self.job_title+self.company_name+self.location+self.keywords+'&salary=+'self.salary+'&salary-option=on&job-posted=0&src=1&ojs=4'

	
