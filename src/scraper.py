import requests
from bs4 import BeautifulSoup
from src.paper import Paper


class Scraper:
    def __init__(self, query):
        self.query = query
        self.url = 'https://scholar.google.com/scholar?as_sdt=0%2C5&q=' + '+'.join(self.query)
        self.results = None
        self.page = None

    def fetch_page(self):
        content = requests.get(self.url).text
        self.page = BeautifulSoup(content, 'lxml')


    def retrieve(self):
        self.fetch_page()
        results = []
        for entry in self.page.find_all("h3", attrs={"class": "gs_rt"}):
            results.append(Paper(title=entry.a.text, link=entry.a['href']))
        self.results = results
        return results