import mysql.connector
from raw_crud import delete_sth
from raw_crud import display_tables
from raw_crud import if_string_to_SQL

class Delete:
    def delete_rows(self, conn):
        all_tables = display_tables(conn)

        for i in range(len(all_tables)):
            print(all_tables[i].upper(), end=" | ")

        chosen_table = input("\nIn which table you want to delete a rows? Choose one: ")

        if chosen_table in all_tables:
            where_condition = input("Insert where condition(SQL format):")



        delete_sth(conn, chosen_table, where_condition)