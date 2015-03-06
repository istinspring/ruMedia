import logging
from grab.spider import Spider


logger = logging.getLogger(__name__)


class VottSpider(Spider):
    base_url = 'http://vott.ru/'
    initial_urls = [base_url]

    xpaths = {
        'list': '///div[contains(@id, "entry_") and not(@class)]',
        'article-title': './/div[@class="entry"]/a[@class="title"]',
        'article-votes': './/div[@class="vote"]/a',
    }

    def process_data(self, data):
        pass

    def task_initial(self, grab, task):
        print grab.doc.select(u'//title').text()

        articles = grab.doc.select(self.xpaths['list'])

        for article in articles:
            title = article.select(self.xpaths['article-title']).text(default=u'')
            votes = article.select(self.xpaths['article-votes']).text(default=u'')

            logger.info(u"[{}] {}".format(votes, title))
