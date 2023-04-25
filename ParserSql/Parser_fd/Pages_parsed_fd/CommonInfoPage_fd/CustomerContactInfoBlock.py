class CustomerContactInfoBlock:  # div class=container

    def __init__(self, soup):
        customer_contact_info_block = soup.find_all('div', 'col')[1].get_text(strip=True, separator="|").split("|")  # [1] - customer_contact_info_block
        self.procurement_customer_address = self.get_address(customer_contact_info_block)  # Российская Федерация, 663491, Красноярский край, Кежемский р-н, Кодинск г, Гидростроителей, Д. 26
        self.procurement_customer_region = self.get_region(customer_contact_info_block)  # Красноярский край

    def get_region(self, customer_contact_info_block):
        idx_key_region = customer_contact_info_block.index("Регион")
        return customer_contact_info_block[idx_key_region + 1]

    def get_address(self, customer_contact_info_block):
        idx_key_address = customer_contact_info_block.index("Место нахождения")
        return customer_contact_info_block[idx_key_address + 1]


if __name__ == '__main__':
    import requests
    from bs4 import BeautifulSoup

    url = 'https://zakupki.gov.ru/epz/order/notice/ea20/view/common-info.html?regNumber=0319300312223000162'
    user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0')

    html_content = requests.get(url, timeout=(100, 100), headers={'User-Agent': user_agent})
    html_content = html_content.content.decode(encoding='utf-8')
    soup_content = BeautifulSoup(html_content, 'html.parser')

    customer_contact_info_block = soup_content.find_all(
        'div', 'col')[1].get_text(strip=True, separator="|").split("|")
    idx_key_region = customer_contact_info_block.index("Место нахождения")
    print(customer_contact_info_block[idx_key_region + 1])


"""  File "D:\IT_scholarship\My_python_apps\Diplom_Pharmabot\Parser_Bd\Parser_fd\Pages_parsed_fd\CommonInfoPage.py", line 14, in __init__
    self.CustomerContactInfoBlock = CustomerContactInfoBlock(soup)
  File "D:\IT_scholarship\My_python_apps\Diplom_Pharmabot\Parser_Bd\Parser_fd\Pages_parsed_fd\CommonInfoPage_fd\CustomerContactInfoBlock.py", line 5, in __init__
    self.procurement_customer_address = self.get_address(customer_contact_info_block)  # Российская Федерация, 663491, Красноярский край, Кежемский р-н, Кодинск г, Гидростроителей, Д. 26
  File "D:\IT_scholarship\My_python_apps\Diplom_Pharmabot\Parser_Bd\Parser_fd\Pages_parsed_fd\CommonInfoPage_fd\CustomerContactInfoBlock.py", line 13, in get_address
    idx_key_address = customer_contact_info_block.index("Место нахождения")
  File "D:\IT_scholarship\My_python_apps\Diplom_Pharmabot\Parser_Bd\venv\lib\site-packages\bs4\element.py", line 1541, in index
    raise ValueError("Tag.index: element not in tag")
ValueError: Tag.index: element not in tag"""