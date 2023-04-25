class ProcurementObjectBlock:  # div class=container id=positionKTRU

    def __init__(self, soup):
        # procurement_object_block = soup.find_all('div', 'col')[3]  # [3] - тут не работает

        # div class=blockInfo__title - Информация об объекте закупки
        # div class=blockInfo__section section
        #  div class=section__title
        self.key_no_volume = None  # Невозможно определить количество (объем) закупаемых товаров, работ, услуг
        #   div class=section__info
        self.no_volume_yes_no = False  # Да

        #  div class=section__info error
        self.no_volume_message = None  # В соответствии c ч. 24 ст. 22 Закона № 44-ФЗ «О контрактной системе в сфере закупок
        # товаров, работ, услуг для обеспечения государственных и муниципальных нужд» оплата поставки товара, выполнения
        # работы или оказания услуги осуществляется по цене единицы товара, работы, услуги исходя из количества товара,
        # поставка которого будет осуществлена в ходе исполнения контракта, объема фактически выполненной работы или
        # оказанной услуги, но в размере, не превышающем максимального значения цены контракта указанного в приглашении
        # на участие в закупке и документации о закупке.

        self.procurement_object = list()
