import mysql.connector
from create import Create
from read import Read
from update import Update
from delete import Delete
from raw_crud import connection_to_server

conn = connection_to_server(datab="world") #Default localhost i połączenie z bazą TheShips

if conn:
    while True:
        print('c=Create, r=Read, u=Update, d=Delete, anything else=Exit ')
        choice = input('What do you want to do? Choose one option:  ')


        if choice == 'c':
            create1 = Create()
            create1.insert_row(conn)
        elif choice == 'r':
            read1 = Read()
            read1.display_table(conn)
        elif choice == 'u':
            update1 = Update()
            update1.update_rows(conn)
        elif choice == 'd':
            delete1 = Delete()
            delete1.delete_rows(conn)
        else:
            print('Bye :)')
            break

else:
    print('Failed to connect to database')