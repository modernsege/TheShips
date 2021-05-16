import mysql.connector
from raw_crud import display_sth
from raw_crud import display_columns
from raw_crud import display_tables



class Read:
    def display_table(self, conn):
        all_tables = display_tables(conn)

        for i in range(len(all_tables)):
            print(all_tables[i].upper(), end=" | ")

        chosen_table = input("\nWhat table to display: ")

        if chosen_table in all_tables:
            all_columns = display_columns(conn, chosen_table, 'world')

            for i in range(len(all_columns)):
                all_columns[i] = all_columns[i].upper()
                print(all_columns[i], end="\t")

            chosen_columns = input("\nWhat columns to display (if u want more than one write next after comma): ")
            user_choice = input("Do you want to add conditions to your query?(y/n)")
            where_condition = ""
            group_by = ""
            if user_choice == 'y':
                where_condition = input("Insert condition(SQL format):")

            if where_condition == "":
                where_condition = True
            user_choice = input("Do you want to add grouping to your query?(y/n)")
            if user_choice == "y":
                while True:
                    condition_column = input("Choose column you want to group by: ")
                    if condition_column in all_columns:
                       group_by += condition_column
                    else:
                        break

                    continues_choice = input("Do you want to add another column for grouping?? (y/n)")
                    if continues_choice == "y":
                        group_by += ", "
                    else:
                        break
            if group_by == "":
                group_by = None


            result = display_sth(conn, chosen_table, chosen_columns, where_condition, group_by)
            for i in range(len(result)):
                for j in range(len(result[0])):
                    print(result[i][j], end = " | ")
                print("")
        else:
            print("Table does not exist")

