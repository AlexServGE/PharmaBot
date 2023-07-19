import sqlite3
import os
from sqlite3 import Error


class SqlApiIns:

    def __init__(self):
        self.con = self.establish_sql_connection()
        self.create_daily_procurements_table()

    def establish_sql_connection(self):
        try:
            con = sqlite3.connect(os.path.join(os.path.split(os.getcwd())[0], "ProcurementsDB\\Procurements.db"))
            print("Connection is established: Database is created in memory")
            return con
        except Error:
            print(Error)

    # Необходимо добавить столбец "Категория лекарственных препаратов"
    def create_daily_procurements_table(self):
        cursorObj = self.con.cursor()
        cursorObj.execute(
            "CREATE TABLE if not exists "
            "daily_new_procurements("
            "id integer PRIMARY KEY AUTOINCREMENT, "
            "procurement_id VARCHAR(45), "
            "procurement_link VARCHAR(45), "
            "procurement_object VARCHAR(45), "
            "procurement_customer VARCHAR(45), "
            "procurement_federal_region VARCHAR(45),"
            "procurement_region VARCHAR(45),"
            "procurement_publication_date VARCHAR(45),"
            "procurement_due_date VARCHAR(45),"
            "procurement_total_value VARCHAR(45),"
            "UNIQUE(procurement_id)"
            ")")
        self.con.commit()

    def sql_insert_daily_procurements(self, entities):
        cursorObj = self.con.cursor()
        cursorObj.execute(
            'INSERT INTO daily_new_procurements('
            'procurement_id, '
            'procurement_link, '
            'procurement_object, '
            'procurement_customer, '
            'procurement_federal_region,'
            'procurement_region,'
            'procurement_publication_date,'
            'procurement_due_date,'
            'procurement_total_value'
            ') '
            'VALUES('
            '?, ?, ?, ?, ?,?,?,?,?)',
            entities)
        self.con.commit()


if __name__ == '__main__':
    import os

    print(os.path.join(os.path.split(os.path.split(os.getcwd())[0])[0], "ProcurementsDB\\Procurements.db"))
    pass
