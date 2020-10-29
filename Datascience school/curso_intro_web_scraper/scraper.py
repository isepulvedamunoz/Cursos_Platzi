import requests
import lxml.html as html
import os
import datetime

HOME_URL = 'https://www.publimetro.cl/cl/'

XPATH_LINK_TO_ARTICLE = '//div[@class="cont_378_e_2015"]//h3/a/text()'
XPATH_TITLE = '//h1[@id="cuDetalle_cuTitular_tituloNoticia"]/text()'
XPATH_SUMMARY = '//h2[@id="cuDetalle_cuTitular_bajadaNoticia"]/text()'
XPATH_CUERPO = '//div[@class="EmolText"]/div/text()'


def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"','')
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                date = parsed.xpath(XPATH_DATE)[0]
            except IndexError:
                return

            with open(f'{today}/{title}.txt','w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                f.write(date)

        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            # print(links_to_notices)
            today = datetime.date.today().strftime('%d-%m-%Y')

            if not os.path.isdir(today):
                os.mkdir(today)
            
            for link in links_to_notices:
                parse_notice(link, today)

        else:
            raise ValueError(f'Error: {response.status_code}')


    except ValueError as ve:
        print(ve)

def run():
    parse_home()


if __name__ == "__main__":
    run()