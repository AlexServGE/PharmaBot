from Parser_fd.RawWebPage import RawWebPage
from Parser_fd.Crawler_fd.SearchEnginePage import SearchEnginePage
from Parser_fd.Pages_parsed_fd.CommonInfoPage import CommonInfoPage
from sqlite3 import IntegrityError
from SqlApiIns_fd.SqlApiIns import SqlApiIns
from datetime import datetime, timedelta
import urllib.parse


class ControllerDailyProcurements:

    def __init__(self, inn_medicine_list_filter, federal_region_dict):
        self.procurements_db = SqlApiIns()
        self.pharmbot_ver001_INN_list_session(inn_medicine_list_filter, federal_region_dict)

    def pharmbot_ver001_INN_list_session(self, inn_medicine_list_filter, federal_region_dict):
        for inn_medicine in inn_medicine_list_filter:
            # inn_medicine_url_coded = urllib.parse.quote(inn_medicine)

            today = datetime.today().date().strftime("%d.%m.%Y")
            yesterday_datetime = datetime.today().date() - timedelta(days=1)
            yesterday = yesterday_datetime.strftime("%d.%m.%Y")
            url_search_engine = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?' \
                                'morphology=on&sortBy=UPDATE_DATE&pageNumber=1' \
                                '&sortDirection=false&recordsPerPage=_100' \
                                '&showLotsInfoHidden=false&fz44=on&af=on' \
                                '&priceContractAdvantages44IdNameHidden=%7B%7D' \
                                '&priceContractAdvantages94IdNameHidden=%7B%7D' \
                                '&currencyIdGeneral=-1' \
                                f'&publishDateFrom={yesterday}' \
                                f'&publishDateTo={today}' \
                                '&selectedSubjectsIdNameHidden=%7B%7D' \
                                '&okdpGroupIdsIdNameHidden=%7B%7D' \
                                '&koksIdsIdNameHidden=%7B%7D' \
                                f'&mnnFarmNameIdMap={inn_medicine}' \
                                '&OrderPlacementSmallBusinessSubject=on&OrderPlacementRnpData=on&OrderPlacementExecutionRequirement=on' \
                                '&orderPlacement94_0=0&orderPlacement94_1=0&orderPlacement94_2=0&contractPriceCurrencyId=-1' \
                                '&budgetLevelIdNameHidden=%7B%7D' \
                                '&nonBudgetTypesIdNameHidden=%7B%7D&gws=%D0%92%D1%8B%D0%B1%D0%B5%D1%80%D0%B8%D1%82%D0%B5+%D1%82%D0%B8%D0%BF+%D0%B7%D0%B0%D0%BA%D1%83%D0%BF%D0%BA%D0%B8'

            raw_search_engine_page = RawWebPage(url_search_engine)  # возможно стоит добавить обработку иключений
            search_engine_page = SearchEnginePage(raw_search_engine_page.soup_content)
            self.pharmbot_ver001_INN_session(search_engine_page, federal_region_dict)

    def pharmbot_ver001_INN_session(self,
                                    search_engine_page, federal_region_dict):
        """Создает list c tuples, который затем передает в базу данных"""
        process_workload = search_engine_page.search_results_dict

        for procurement_id, procurement_link in process_workload.items():
            # можно добавить логи здесь
            raw_procurement_page = RawWebPage(procurement_link)
            common_info_page = CommonInfoPage(raw_procurement_page.soup_content)
            today_procurement_tuple = (
                (procurement_id,
                 procurement_link,
                 common_info_page.MainInfoHeader.object,
                 common_info_page.MainInfoHeader.customer,
                 federal_region_dict[common_info_page.CustomerContactInfoBlock.procurement_customer_region],
                 common_info_page.CustomerContactInfoBlock.procurement_customer_region,
                 common_info_page.MainInfoHeader.sdate,
                 common_info_page.MainInfoHeader.edate,
                 common_info_page.MainInfoHeader.tvalue)
            )
            try:
                self.procurements_db.sql_insert_daily_procurements(today_procurement_tuple)
            except IntegrityError as e:
                print(
                    f"IntegrityError occurred, while sqlite INSERT {today_procurement_tuple[0]}. This procurement is already in the db")