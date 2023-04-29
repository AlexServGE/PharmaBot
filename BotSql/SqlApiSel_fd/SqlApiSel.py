import sqlite3
from sqlite3 import Error
from datetime import datetime, timedelta


class SqlApiSel:

    def __init__(self):
        self.con = self.establish_sql_connection()

    def establish_sql_connection(self):
        try:
            con = sqlite3.connect('..\ProcurementsDB\Procurements.db')
            print("Connection is established: Database is created in memory")
            return con
        except Error:
            print(Error)

    def sql_select_daily_procurements(self,user_filters):
        cursorObj = self.con.cursor()

        today = datetime.today().date().strftime("%d.%m.%Y")
        yesterday_datetime = datetime.today().date() - timedelta(days=1)
        yesterday = yesterday_datetime.strftime("%d.%m.%Y")

        cursorObj.execute(f'SELECT procurement_id,procurement_publication_date,procurement_customer,procurement_total_value,procurement_object,procurement_link FROM daily_new_procurements WHERE procurement_federal_region = "{user_filters[1]}" AND procurement_publication_date BETWEEN "{yesterday}" AND "{today}"') ## необходимо использовать функцию, которая передаёт текущий день в where
        selected_data_list = cursorObj.fetchall()
        return selected_data_list


if __name__ == '__main__':
    sql_api_sel = SqlApiSel()
    print(sql_api_sel.sql_select_daily_procurements())


