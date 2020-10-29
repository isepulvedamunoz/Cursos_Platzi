import requests
import bs4
from common import config


class HomePage:

    def __init__(self, news_site:uid, url):
        self._config = config()['news_sites'][news_site_uid]
        self._queries = self._config['queries']
        self._html = None

        self._visit(url)

    @property
    def article_links(self):
        link_list = []
        for link in self._select
    
    def _select(self, query_string):
        return self._html.select(query_string)

    def _visit(self, url):
        response = requests.get(url)

        response.raise_for_status()

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')
