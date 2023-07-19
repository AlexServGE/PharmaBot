import requests
from bs4 import BeautifulSoup


class RawWebPage:

    def __init__(self, url):
        self.html_content = self.get_webpage(url)
        self.soup_content = self.get_soup(self.html_content)

    def get_webpage(self, url):
        user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0')
        webpage = requests.get(url, timeout=(100, 100), headers={'User-Agent': user_agent})
        return webpage.content.decode(encoding='utf-8')

    def get_soup(self, html_content):
        return BeautifulSoup(html_content, 'html.parser')


if __name__=='__main__':
    url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=%D0%B9%D0%BE%D0%B3%D0%B5%D0%BA%D1%81%D0%BE%D0%BB&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&af=on&currencyIdGeneral=-1&publishDateFrom=21.04.2023&applSubmissionCloseDateFrom=21.04.2023'

    raw_web_page = RawWebPage(url)

    # for el in raw_web_page.soup_content.find_all('a'):
    #     print(type(el))


    tag = raw_web_page.soup_content.find('p')
    print(tag.find('a'))

    # print(raw_web_page.soup_content.find_all("div", "registry-entry__header-mid__number")[0].get_text(strip=True))
    # print(raw_web_page.soup_content.find_all("div", "registry-entry__header-mid__number")[0].find_all("a")[0].get("href"))