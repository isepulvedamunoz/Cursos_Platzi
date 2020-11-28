import requests
from bs4 import BeautifulSoup


link = requests.get('https://www.pagina12.com.ar/secciones/deportes')

sports = BeautifulSoup(link.text, 'lxml')


def noticias(soup):

    """ Funcion que devuelve los links de las noticias deportivas de un diario argentino,
        mediante BeautifulSoup"""

    news = soup.find_all('div', attrs={'class':'article-item__content'})

    links_news = [new.a.get('href') for new in news]

    print(links_news)


if __name__ == '__main__':
    noticias(sports)