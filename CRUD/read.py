import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="hr"
)


class Read:
    def read_biggest_salaries_from_employees(self): #wypisanie imie, nazwiska i wynagrodzenia pracowników, których pensja jest wieksza niż 10000
        cursor = conn.cursor()
        query = "select first_name, last_name, salary from employees where salary > 10000"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
