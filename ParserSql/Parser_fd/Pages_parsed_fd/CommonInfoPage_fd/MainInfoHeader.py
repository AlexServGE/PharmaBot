class MainInfoHeader:  # div class=cardMainInfo row

    def __init__(self, soup):
        # div class=sectionMainInfo borderRight col-6

        tags = {"fl_type": "cardMainInfo__title d-flex text-truncate",
                "id_status": "cardMainInfo__status",
                "object_customer": "sectionMainInfo__body",
                "tvalue_sdate_udate_edate": "sectionMainInfo borderRight col-3 colSpaceBetween",
                "external_links": "sectionMainInfo col-3 colSpaceBetween mt-auto rel-links"}

        #    div class=cardMainInfo__title d-flex text-truncate
        self.federal_law = self.get_tag_content(soup, tags["fl_type"], 0)  # 44-ФЗ
        self.type = self.get_tag_content(soup, tags["fl_type"], 1)  # Электронный аукцион
        #  div class=cardMainInfo__status
        self.id = self.get_tag_content(soup, tags["id_status"], 0)  # № 0820500000823002573
        self.status = self.get_tag_content(soup, tags["id_status"], 1)  # Подача заявок
        # div class=sectionMainInfo__body
        self.object = self.get_tag_content(soup, tags["object_customer"], 0)  # № МНН: ЙОГЕКСОЛ
        self.customer = self.get_tag_content(soup, tags["object_customer"], 1)  # КРАЕВОЕ ГОСУДАРСТВЕННОЕ КАЗЕННОЕ УЧРЕЖДЕНИЕ "ЦЕНТР ГОСУДАРСТВЕННЫХ ЗАКУПОК ПРИМОРСКОГО КРАЯ"
        # div class=sectionMainInfo borderRight col-3 colSpaceBetween
        self.tvalue = self.get_tag_content(soup, tags["tvalue_sdate_udate_edate"], 0)  # 197\xa0188,20 ₽
        self.sdate = self.get_tag_content(soup, tags["tvalue_sdate_udate_edate"], 1)  # 25.04.2023
        self.udate = self.get_tag_content(soup, tags["tvalue_sdate_udate_edate"], 2)  # 25.04.2023
        self.edate = self.get_tag_content(soup, tags["tvalue_sdate_udate_edate"], 3)  # 04.05.2023
        # div class=sectionMainInfo col-3 colSpaceBetween mt-auto rel-links
        # self.external_links = soup.find_all('div', 'sectionMainInfo col-3 colSpaceBetween mt-auto rel-links')[
        #     0].get_text(strip=True,
        #                 separator="|").replace(
        #     " ", "").replace("\n", "").split(
        #     "|")  # ПозицияКТРУ|Позицияплана-графика|Контракт|Жалоба|Внеплановаяпроверка

    def get_tag_content(self, soup, tag, index):
        if tag == "sectionMainInfo__body" or tag == "sectionMainInfo borderRight col-3 colSpaceBetween":
            return soup.find_all('div', tag)[0].get_text(strip=True, separator="|").split("|")[1::2][index]
        else:
            return soup.find_all('div', tag)[0].get_text(strip=True, separator="|").split("|")[index]


if __name__ == '__main__':
    import requests
    from bs4 import BeautifulSoup

    url = 'https://zakupki.gov.ru/epz/order/notice/ea20/view/common-info.html?regNumber=0820500000823002573'
    user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0')

    html_content = requests.get(url, timeout=(100, 100), headers={'User-Agent': user_agent})
    html_content = html_content.content.decode(encoding='utf-8')
    soup_content = BeautifulSoup(html_content, 'html.parser')

    print(
        soup_content.find_all('div', 'cardMainInfo__title d-flex text-truncate')[0].get_text(strip=True,
                                                                                             separator="|").split("|"))
    print(soup_content.find_all('div', 'cardMainInfo__status')[0].get_text(strip=True, separator="|").split("|"))
    print(soup_content.find_all('div', 'sectionMainInfo__body')[0].get_text(strip=True, separator="|").split("|")[1::2])
    print(soup_content.find_all('div', 'sectionMainInfo borderRight col-3 colSpaceBetween')[0].get_text(strip=True,
                                                                                                        separator="|").split(
        "|")[1::2])
    print(
        soup_content.find_all('div', 'sectionMainInfo col-3 colSpaceBetween mt-auto rel-links')[0].get_text(strip=True,
                                                                                                            separator="|").replace(
            " ", "").replace("\n", "").split("|"))
