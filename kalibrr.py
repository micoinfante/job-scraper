import requests
import bs4


class Kalibrr(object):
	"""
		This should return the information about a job listing on kalibrr 
		including the job title, company name, summary, salary if available 
		and location.
		Kalibrr has an API you can use it to query a data or you can use python requests, 
		the request returns a json format data so no need to use BeautfulSoup
	"""
	
	def __init__(self, job_title, company_name, location,summary, salary, keywords):
		self.job_title     = job_title
		self.company_name  = company_name
		self.location      = location
		self.summary       = summary
		self.keywords      = keywords

	def check_access(self):
		"""
		this is just for debugging purposes:
		if the server refuses to give access use headers as a work-around. 
		The server identified your script as a non-default browser (Chrome, Firefox, etc.) and 
		is refusing to "speak" with it. 
		It's very common to see sites doing this to avoid scrapers, exactly what you're trying to do...
		"""
		url = 'https://www.kalibrr.com/api/job_board/search?limit=15&location=Manila&offset=0&salary_gte=1000&salary_interval=monthly&text='
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
		page = requests.get(url, headers = headers).json()
		print(page)

k = Kalibrr('a', 'a', 'a', 'a', 'a', 'a')
k.check_access()


