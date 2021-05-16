import mysql.connector
from raw_crud import insert_record
from raw_crud import display_columns
from raw_crud import display_tables
from raw_crud import if_string_to_SQL

class Create:
    def insert_row(self, conn):
        all_tables = display_tables(conn)

        for i in range (len(all_tables)):
            all_tables[i] = all_tables[i].upper()
            print(all_tables[i], end=" | ")
        chosen_table = input("\nIn which table you want to insert sth? Choose one: ")
        chosen_table = chosen_table.upper()


        if chosen_table in all_tables:
            all_columns = display_columns(conn, chosen_table, 'world')

            for i in range(len(all_columns)):
                all_columns[i] = all_columns[i].upper()
                print(all_columns[i], end=" | ")

            values = []
            print("\nInsert values to columns:")
            for i in range(len(all_columns)):
                value = input(f'{all_columns[i]}:')
                value = if_string_to_SQL(value)
                values.append(value)

            sql_values = ""
            for i in range(len(all_columns)):
                if i < (len(all_columns) - 1):
                    sql_values += values[i] + ", "
                else:
                    sql_values += values[i]

            insert_record(conn, chosen_table, sql_values)

        else:
            print("Table does not exist")