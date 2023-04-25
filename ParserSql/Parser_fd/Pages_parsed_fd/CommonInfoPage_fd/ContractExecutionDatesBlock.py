class ContractExecutionDatesBlock:  # div class=container

    def __init__(self, soup):
        # div class=blockInfo__title - Информация о сроках исполнения контракта и источниках финансирования
        # div class=blockInfo__section
        #  div class=blockInfo__section
        #   div class=section__title
        self.key_contract_execution_start = None  # Дата начала исполнения контракта
        #   div class=section__info
        self.contract_execution_start = None  # 10  календарных дней с даты заключения контракта

        #   div class=section__title
        self.key_contract_execution_duration = None  # Срок исполнения контракта
        #   div class=section__info
        self.contract_execution_duration = None  # 44  календарных дней с даты начала исполнения контракта
