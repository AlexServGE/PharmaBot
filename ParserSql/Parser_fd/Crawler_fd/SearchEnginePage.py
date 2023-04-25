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
    pass
