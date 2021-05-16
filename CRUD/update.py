from raw_crud import update_sth
from raw_crud import display_tables
from raw_crud import display_columns
from raw_crud import if_string_to_SQL
class Update:
    def update_rows(self, conn):
        while True:   
            user_choice = input("1.Update row - update rows in one column\n2.Update rows (detailed) - Update rows in many columns\nAnything else. Exit\nWhat do you want to do: ")
            if user_choice == '2':
                self.update_rows_detailed(conn)
            
            elif user_choice == '1':
                self.update_row(conn)
            
            else:
                break

    def update_rows_detailed(self, conn):
        all_tables = display_tables(conn)
        for i in range (len(all_tables)):
            all_tables[i] = all_tables[i].upper()
            print(all_tables[i], end=" | ")
        chosen_table = input("What table to update: ")
        chosen_table = chosen_table.upper()

        if chosen_table in all_tables:
            all_columns=display_columns(conn, chosen_table)
            for i in range (len(all_columns)):
                all_columns[i] = all_columns[i].upper()
                print(all_columns[i], end=" | ")
            change = ""
            while True:
                chosen_column = input("Choose column you want to update: ")
                chosen_column = chosen_column.upper()

                if chosen_column in all_columns:
                    value = input("Choose value you want to change to: ")
                    value = if_string_to_SQL(value)

                    change += chosen_column + "=" + value
                    continue_choice = input("Do you want to add set another column? (y/n)")
                    if continue_choice == "y":
                        change += ", "
                    else:
                        break
                else:
                    print("Column does not exist")

            where_condition = input("Insert condition(SQL format): ")
            if where_condition == "":
                where_condition = True
            update_sth(conn, chosen_table, change, where_condition)
        else:
            print("Table does not exist")

    def update_row(self,conn):
        all_tables = display_tables(conn)
        for i in range (len(all_tables)):
            all_tables[i] = all_tables[i].upper()
            print(all_tables[i], end=" | ")
        chosen_table = input("What table to display: ")
        chosen_table = chosen_table.upper()

        if chosen_table in all_tables:
            all_columns=display_columns(conn, chosen_table)
            for i in range (len(all_columns)):
                all_columns[i] = all_columns[i].upper()
                print(all_columns[i], end=" | ")
            chosen_column = input("Choose column you want to update: ").upper()
            if chosen_column in all_columns:
                value = input("Choose value you want to change to: ")
                value = if_string_to_SQL(value)

                where_condition = input("Insert condition(SQL format): ")
                if where_condition == "":
                    where_condition = True

                change = chosen_column + "=" + value

                update_sth(conn, chosen_table, change, where_condition)
            else:
                print("Column does not exist")
        else:
            print("Table does not exist")

        