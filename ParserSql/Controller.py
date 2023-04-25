from Parser_fd.RawWebPage import RawWebPage
from Parser_fd.Crawler_fd.SearchEnginePage import SearchEnginePage
from Parser_fd.Pages_parsed_fd.CommonInfoPage import CommonInfoPage
from SqlApiIns_fd.SqlApiIns import SqlApiIns


class Controller:

    def __init__(self, url_search_engine):
        self.raw_search_engine_page = RawWebPage(url_search_engine)  # возможно стоит добавить обработку иключений
        self.search_engine_page = SearchEnginePage(self.raw_search_engine_page.soup_content)
        self.procurements_db = SqlApiIns()
        self.pharmbot_ver001_session()

    def pharmbot_ver001_session(self):  # возможно следует сделать отдельные классы для каждого из ботов
        """Создает list c tuples, который затем передает в базу данных"""
        process_workload = self.search_engine_page.search_results_dict
        today_procurements_list = list()
        for procurement_id, procurement_link in process_workload.items():
            # можно добавить логи здесь
            raw_procurement_page = RawWebPage(procurement_link)
            common_info_page = CommonInfoPage(raw_procurement_page.soup_content)
            today_procurements_list.append(
                (procurement_id,
                 procurement_link,
                 common_info_page.MainInfoHeader.object,
                 common_info_page.MainInfoHeader.customer,
                 common_info_page.CustomerContactInfoBlock.procurement_customer_region,
                 common_info_page.MainInfoHeader.sdate,
                 common_info_page.MainInfoHeader.edate,
                 common_info_page.MainInfoHeader.tvalue)
            )
        # for el in today_procurements_list:
        #     print(el)
        self.procurements_db.sql_insert_daily_procurements(today_procurements_list)


