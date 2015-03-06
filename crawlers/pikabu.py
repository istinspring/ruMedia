import logging
from grab.spider import Spider


logger = logging.getLogger(__name__)


class PikabuSpider(Spider):
    base_url = 'http://pikabu.ru/'
    initial_urls = [base_url]

    xpaths = {
        'list': '//table[contains(@id, "inner_wrap_")]',
        'article-title': './/a[contains(@class, "b-story__link")]',
        'article-votes': './/ul[@class="b-rating"]/li[contains(@id, "num_digs")]',
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
