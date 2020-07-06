from src.paper import Paper
from src.scraper import Scraper
from src.rss import RSS

class ScholarBot:
    def __init__(self, query, title, out_xml):
        self.query = query
        self.title = title
        self.out = out_xml

    def activate(self):
        s = Scraper(self.query)
        papers = s.retrieve()
        r = RSS(self.title, papers, self.out)
        r.write_rss()