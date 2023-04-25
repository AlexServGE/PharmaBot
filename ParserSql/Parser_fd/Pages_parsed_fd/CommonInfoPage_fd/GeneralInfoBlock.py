class GeneralInfoBlock:  # div class=container

    def __init__(self, soup):
        general_info_block = soup.find_all('div', 'col')[0].get_text(strip=True, separator="|").split("|") #[0] - general_info_block

        # div class=blockInfo__title - Общая информация о закупке
        # div class=blockInfo__section section
        #  div class=section__title
        self.key_procurement_platform = None  # Наименование электронной площадки в информационно-телекоммуникационной сети «Интернет»
        #  div class=section__info
        self.procurement_platform = None  # ЭТП Газпромбанк

        #  div class=section__title
        self.key_procurement_platform_link = None  # Адрес электронной площадки в информационно-телекоммуникационной сети «Интернет»
        #  div class=section__info
        self.procurement_platform_link = None  # https://etpgpb.ru/
