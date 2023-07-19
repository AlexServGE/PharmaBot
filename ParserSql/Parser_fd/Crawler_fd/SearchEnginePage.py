class SearchEnginePage:

    def __init__(self, soup):
        # class="registry-entry__header-mid__number"

        self.search_results_dict = self.get_dict_search_results(soup)

    def get_dict_search_results(self, soup):
        """
        Функция берёт страницу: https://zakupki.gov.ru/epz/order/extendedsearch/results.html?
        Опции: Могут быть использованы любые фильтры поиска.
        Параметры: soup вебстраницы
        Возвращает: словарь dict_search_results {String procurement_id: String procurement_link}
        """
        soup_search_results = soup.find_all("div", "registry-entry__header-mid__number")
        dict_search_results = dict()
        for procurement in soup_search_results:
            procurement_id = procurement.get_text(strip=True)
            procurement_link = f'https://zakupki.gov.ru/{procurement.find_all("a")[0].get("href")}'
            dict_search_results[procurement_id] = procurement_link
        return dict_search_results




if __name__ == '__main__':
    from Parser_fd.RawWebPage import RawWebPage
    url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=%D0%B9%D0%BE%D0%B3%D0%B5%D0%BA%D1%81%D0%BE%D0%BB&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&af=on&currencyIdGeneral=-1'
    raw_search_engine_page = RawWebPage(url)
    search_engine_page = SearchEnginePage(raw_search_engine_page.soup_content)
    for el in search_engine_page.search_results_dict.items():
        print(el)
