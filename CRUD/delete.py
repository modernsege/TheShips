import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="hr"
)


class Delete:
    def func_DeleteData(self):
        job_idv = input('Podaj job_id elementu, który chcesz usunąć: ')

        query = "select * from jobs where job_id = %s"
        data = [job_idv]
        cursor = conn.cursor()
        cursor.execute(query, data)
        item_to_delete = cursor.fetchone()
        print('job_id: {}\njob_title: {}\nmin_salary {}\nmax_salary {}'.format(item_to_delete[0], item_to_delete[1], item_to_delete[2], item_to_delete[3]))
        confirm = input('Czy na pewno usunąć? (y/n)')

        if confirm == 'y':
            deleteQuery = "delete from jobs where job_id = %s"
            cursor.execute(deleteQuery, data)
            conn.commit()
            print("Powodzenie!")
        elif confirm == 'n':
            print("Usunięcie danych nie powiodło się")
        else:
            print("Nieznane polecenie")

        conn.close()