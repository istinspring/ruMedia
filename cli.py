import logging
from grab.tools.logs import default_logging

from crawlers.news2 import News2Spider
from crawlers.pikabu import PikabuSpider
from crawlers.vott import VottSpider
from settings import DB_NAME


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def run_spider(spider_class, use_proxy=False, use_cache=True, **kwargs):
    """ Configure and run bot instance.

    """

    options = {
        'thread_number': 3,
        'network_try_limit': 5,
        'task_try_limit': 5,
        'max_task_generator_chunk': 1,
        'priority_mode': 'const',
    }

    bot = spider_class(**options)

    if use_proxy:
        # need proxy list
        bot.load_proxylist('proxylist.txt', 'text_file', 'http', auto_change=True)
    if use_cache:
        # need mongodb
        bot.setup_cache(backend='mongo', database=DB_NAME, use_compression=True)

    bot.setup_grab(timeout=60, connect_timeout=60)

    for key, value in kwargs.items():
        setattr(bot, key, value)

    bot.run()
    return bot


if __name__ == '__main__':
    default_logging()
    run_spider(PikabuSpider)
    run_spider(VottSpider)
    run_spider(News2Spider)
