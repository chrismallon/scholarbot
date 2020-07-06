import unittest
from src.scraper import Scraper

class TestScraper(unittest.TestCase):
    def setUp(self) -> None:
        self.query = ['wildlife', 'winners', 'fisher', 'burton']

    def test_that_fetch_page_fetches_something(self):
        s = Scraper(self.query)
        s.fetch_page()
        self.assertIsNotNone(s.page)

    def test_scraper_retrieves_results(self):
        s = Scraper(self.query)
        papers = s.retrieve()
        self.assertEqual(papers[0].title, 'Wildlife winners and losers in an oil sands landscape')
