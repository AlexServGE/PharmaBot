from ControllerDailyProcurements import ControllerDailyProcurements
from Input_configs.Pharma_category.Contrast_media import contrast_media_list_percent_format
from Input_configs.Pharma_category.Antibiotics import antibiotics_list_percent_format
from Input_configs.Pharma_category.Antimicrobs import antimicrobs_list_percent_format
from Input_configs.Federal_regions import federal_regions_dict


class Controller:

    def __init__(self):
        self.pharma_list_percent_format_dict = {
            "21.20.23.112: Вещества контрастные": contrast_media_list_percent_format,
            "21.20.10.190: Препараты противомикробные для системного использования": antimicrobs_list_percent_format,
            "21.20.10.191: Препараты антибактериальные для системного использования": antibiotics_list_percent_format,
        }
        for pharma_category_title, pharma_list_percent_format in self.pharma_list_percent_format_dict.items():
            self.controller_daily_procurements = ControllerDailyProcurements(pharma_list_percent_format,
                                                                             pharma_category_title,
                                                                             federal_regions_dict)
