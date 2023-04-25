from .CommonInfoPage_fd.MainInfoHeader import MainInfoHeader
from .CommonInfoPage_fd.GeneralInfoBlock import GeneralInfoBlock
from .CommonInfoPage_fd.CustomerContactInfoBlock import CustomerContactInfoBlock
from .CommonInfoPage_fd.ProcurementDatesBlock import ProcurementDatesBlock
from .CommonInfoPage_fd.ContractExecutionDatesBlock import ContractExecutionDatesBlock
from .CommonInfoPage_fd.ProcurementObjectBlock import ProcurementObjectBlock


class CommonInfoPage:

    def __init__(self, soup):
        self.MainInfoHeader = MainInfoHeader(soup)
        self.GeneralInfoBlock = GeneralInfoBlock(soup)
        self.CustomerContactInfoBlock = CustomerContactInfoBlock(soup)
        self.ProcurementDatesBlock = ProcurementDatesBlock(soup)
        self.ContractExecutionDatesBlock = ContractExecutionDatesBlock(soup)
        self.ProcurementObjectBlock = ProcurementObjectBlock(soup)


