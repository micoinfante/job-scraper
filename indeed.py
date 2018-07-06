# ["job_title", "company_name", "location", "summary", "salary"]
import bs4
from bs4 import BeautifulSoup
import requests


class Indeed(objct):
	
	def __init__(self, job_title, company_name, location, summary, salary, radius = 25, keywords):
		self.job_title = job_title
		self.company_name = company_name
		self.location = location
		self.summary = summary
		self.salary = salary
		self.radius = radius
		self.keywords = keywords	
		self.URL = 'https://www.indeed.com.ph/jobs?as_and='+ self.job_title
					+'&as_phr=' #exact phrase
					+'&as_any=' + self.keywords
					+'&as_not=' #With none of these words
					+'&as_ttl=' #with these words in the title
					+'&as_cmp=' #company name
					+'&jt=' #job type: internship, new grad, full-time, part-time, 
					+'&st='
					+'&radius=25'
					+'&l='+ self.location
					+'&fromage=any'
					+'&limit=20'
					+'&sort='
					+'&psf=advsrch'
	
	def main():
		page = requests.get(self.URL)
		soup = BeautifulSoup(page.text, "html.parser")
		jobs = get_job_title(soup)
		companies = get_company_name(soup)
		locations = get_location(soup)
		salaries = get_salary(soup)
		summary = get_summary(soup)

	def get_job_title(soup):
		jobs = []
		for div in soup.find_all(name = "div", attrs= {"class" : "row"}):
			for link in div.find_all(name = "a", attrs= {"data-tn-element": "jobTitle"}):
				jobs.append(link["title"])
		return jobs
	
	def get_company_name(soup):
		companies = []
		for div in soup.find_all(name = "div", attrs = {"class" : "row"}):
			company = div.find_all(name = "span", attrs= {"class" : "company"})
			if len(company) > 0:
				for b in company:
					companies.append(b.next.strip)
			else:
				sec_try = div.find_all(name = "span", attrs = {"class" : "result-link-source"})
				for span in sec_try:
					companies.append(span.text.strip())
		return companies

	def get_location(soup):
		locations = []
		spans = soup.find_all(name = "span", attrs = {"class" : "location"})
		for span in spans:
			locations.append(span.text)
		return locations

	def get_salary(soup):
		salaries = []
		for div in soup.find_all(name = "div", attrs = {"class" : "row"}):
			try:
				salaries.append(div.find('nobr').text)
			except:
				try:
					div_two = div.find(name="div", attrs= {"class": "sjcl"})
					div_three = div_two.find("div")
					salaries.append(div.three.text.strip())
				except:
					salaries.append("Nothing Found")
		return salaries

	def get_summary(soup):
		summaries = []
		span = soup.find_all(name = "span", attrs = {"class" : "summary"})
		for span in spans:
			summaries.append(span.text.strip())
		return summaries
