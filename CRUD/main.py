import mysql.connector
from create import Create
from read import Read
from update import Update
from delete import Delete

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="hr"
)

print('c=Create, r=Read, u=Update, d=Delete ')
choice = input('Co chcesz zrobić? Wybierz opcje:  ')

if choice == 'c':
    create1 = Create()
    create1.create_data_in_jobs()
elif choice == 'r':
    read1 = Read()
    read1.read_biggest_salaries_from_employees()
elif choice == 'u':
    pass
    update1 = Update()
    update1.func_UpdateData()
elif choice == 'd':
    delete1 = Delete()
    delete1.func_DeleteData()
else:
    print('Wybrana operacja nie istnieje')

