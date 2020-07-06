import PyRSS2Gen
import datetime

class RSS:
    def __init__(self, title, papers, out):
        self.title = title
        self.papers = papers
        self.rss = None
        self.out = out

    def generate(self):
        self.rss = PyRSS2Gen.RSS2(
            title=self.title,
            description='An RSS feed from google scholar.',
            link=r'https://www.notalink.com/rss',
            lastBuildDate=datetime.datetime.now(),

            items = [PyRSS2Gen.RSSItem(
                title=p.title,
                link=p.link,
                guid=p.link
            ) for p in self.papers]
        )

    def write_rss(self):
        self.generate()
        self.rss.write_xml(open(self.out, 'w'))