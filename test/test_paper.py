import unittest
from src.paper import Paper

class TestPaper(unittest.TestCase):
    def test_paper_attributes(self):
        p = Paper('Wildlife winners and losers in an oil sands landscape',
                  'JT Fisher, AC Burton - Frontiers in Ecology and the …, 2018 - Wiley Online Library',
                  """Energy development and consumption drive changes in global climate, landscapes, and
biodiversity. The oil sands of western Canada are an epicenter of oil production, creating
landscapes without current or historical analogs. Science and policy often focus on pipelines
and species‐at‐risk declines, but we hypothesized that differential responses to
anthropogenic disturbances shift the entire mammal community. Analysis of data collected
from 3 years of camera trapping and species distribution models indicated that …""",
                  'https://esajournals.onlinelibrary.wiley.com/doi/abs/10.1002/fee.1807')
        self.assertEqual(p.title, 'Wildlife winners and losers in an oil sands landscape')
        self.assertEqual(p.authors, 'JT Fisher, AC Burton - Frontiers in Ecology and the …, 2018 - Wiley Online Library')
        self.assertEqual(p.abstract, """Energy development and consumption drive changes in global climate, landscapes, and
biodiversity. The oil sands of western Canada are an epicenter of oil production, creating
landscapes without current or historical analogs. Science and policy often focus on pipelines
and species‐at‐risk declines, but we hypothesized that differential responses to
anthropogenic disturbances shift the entire mammal community. Analysis of data collected
from 3 years of camera trapping and species distribution models indicated that …""")
        self.assertEqual(p.link, 'https://esajournals.onlinelibrary.wiley.com/doi/abs/10.1002/fee.1807')