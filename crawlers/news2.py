import logging
from grab.spider import Spider


logger = logging.getLogger(__name__)


class News2Spider(Spider):
    base_url = 'http://news2.ru/'
    initial_urls = [base_url]

    xpaths = {
        'list': '//div[@class="news_placeholder"]',
        'article-title': './/h3[contains(@id, "news_title")]/a',
        'article-votes': './/div[@class="vote_placeholder"]//div[contains(@id, "vote_num")]/a',
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
