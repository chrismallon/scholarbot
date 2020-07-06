import unittest
import os
from src.rss import RSS
from src.scraper import Scraper

class TestRSS(unittest.TestCase):
    def test_rss_generates_something(self):
        query = ['wildlife', 'winners', 'fisher', 'burton']
        s = Scraper(query)
        papers = s.retrieve()
        rss = RSS('Fisher and Burton Paper', papers, 'test_rss.xml')
        rss.generate()
        self.assertIsNotNone(rss.rss)

    def test_rss_outputs_file(self):
        query = ['wildlife', 'winners', 'fisher', 'burton']
        s = Scraper(query)
        papers = s.retrieve()
        rss = RSS('Fisher and Burton Paper', papers, 'test_rss.xml')
        rss.write_rss()
        self.assertTrue(os.path.isfile('test_rss.xml'))

    def test_rss_has_data(self):
        query = ['wildlife', 'winners', 'fisher', 'burton']
        s = Scraper(query)
        papers = s.retrieve()
        rss = RSS('Fisher and Burton Paper', papers, 'test_rss.xml')
        rss.write_rss()
        found_it = False
        with open('test_rss.xml', 'r') as f:
            for line in f:
                if 'Wildlife winners and losers in an oil sands landscape' in line:
                    found_it = True
        self.assertTrue(found_it)