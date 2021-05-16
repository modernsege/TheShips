import mysql.connector
from raw_crud import delete_sth
from raw_crud import display_tables
from raw_crud import if_string_to_SQL

class Delete:
    def delete_rows(self, conn):
        all_tables = display_tables(conn)

        for i in range (len(all_tables)):
            all_tables[i] = all_tables[i].upper()
            print(all_tables[i], end=" | ")

        chosen_table = input("\nIn which table you want to delete a rows? Choose one: ")
        chosen_table = chosen_table.upper()

        if chosen_table in all_tables:
            where_condition = input("Insert where condition(SQL format):")



        delete_sth(conn, chosen_table, where_condition)
        
        