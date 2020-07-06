import unittest
from src.scraper import Scraper

class TestScraper(unittest.TestCase):
    def test_scraper_retrieves_results(self):
        query = ['wildlife', 'winners', 'fisher', 'burton']
        s = Scraper(query)
        paper = s.retrieve()
