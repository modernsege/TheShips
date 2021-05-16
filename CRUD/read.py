import mysql.connector
from raw_crud import display_sth
from raw_crud import display_columns
from raw_crud import display_tables

class Read:
    def display_table(self, conn):
        
        while True:   
            user_choice = input("1.Quick read - display entire table\n2.Detailed read - where and group by\nAnything else. Exit\nWhat do you want to do: ")
            if user_choice == '1':
                self.display_table_quick(conn)
            
            elif user_choice == '2':
                self.display_table_detailed(conn)
            
            else:
                break

    def display_table_detailed(self, conn):
        
        all_tables = display_tables(conn)
        for i in range (len(all_tables)):
            print(all_tables[i].upper(), end=" | ")
        chosen_table = input("What table to display: ")

        if chosen_table in all_tables:
            all_columns=display_columns(conn, chosen_table, 'world')
            for i in range (len(all_columns)):
                all_columns[i] = all_columns[i].upper()
                print(all_columns[i], end=" | ")

            chosen_columns = input("What columns to display(if u want more than one write next after comma): ")

            user_choice = input("Do you want to add conditions to your query?(y/n)")
            where_condition = ""
            group_by = ""
            if user_choice == "y":
                where_condition = input("Insert condition(SQL format): ")
            if where_condition == "":
                where_condition = True
            user_choice = input("Do you want to add grouping to your query?(y/n)")
            if user_choice == "y":
                while True:
                    condition_column = input("Choose column you want group by: ")
                    if condition_column in all_columns:
                        group_by += condition_column

                    else:
                        break
                    continue_choice = input("Do you want to add another column for grouping? (y/n)")
                    if continue_choice == "y":
                        where_condition += ", "
                    else:
                        break
            if group_by == "":
                group_by = None

            #print(chosen_table)
            #print(chosen_columns)
            #print(where_condition)
            #print(group_by)
            result = display_sth(conn, chosen_table, chosen_columns, where_condition, group_by)
            
            self.display(result)

        else:
            print("Table does not exist")

    def display_table_quick(self, conn):
        all_tables = display_tables(conn)
        for i in range (len(all_tables)):
            print(all_tables[i].upper(), end=" | ")
        chosen_table = input("What table to display: ")

        if chosen_table in all_tables:
            result = display_sth(conn, chosen_table)
            self.display(result)
        else:
            print("Table does not exist")
    
    def display(self, result):
        for i in range (len(result)):
                for j in range (len(result[0])):
                    print(result[i][j], end = " | ")
                
                print("")


        
        