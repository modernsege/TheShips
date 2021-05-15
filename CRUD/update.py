import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="hr"
)

class Update:
    def func_UpdateData(self):
        cursor = conn.cursor()
        employee_idv = input('Podaj employee_id elementu, który chcesz zaktualizować: ')
        choice = input("Chesz zaktualizować wszystkie dane w tabeli (1), czy wybrane (2)? Wpisz 1/2: ")

        if choice == '1':
            print("Wprowadź nowe dane: ")
            first_namev = input("first_name: ")
            last_namev = input("last_name: ")
            emailv = input("email: ")
            phone_numberv = input("phone_number: ")
            hire_datev = input("hire_date: ")
            job_idv = input("job_id: ")
            salaryv = input("salary: ")
            commission_pctv = input("commission_pct: ")
            manager_idv = input("manager_id: ")
            department_idv = input("department_id: ")

            query1 = "update employees set first_name = %s, last_name = %s, email =%s, phone_number =%s, hire_date =%s, job_id =%s, salary =%s, manager_id =%s, department_id =%s where employee_id =%s"
            data1 = [first_namev, last_namev, emailv, phone_numberv, hire_datev, job_idv, salaryv, manager_idv, department_idv, employee_idv]
            cursor.execute(query1, data1)
            conn.commit()
            print("Powodzenie!")

        elif choice == '2':
            field_name = input("Jakie pole chcesz zautualizować? Podaj nazwe: ")
            new_data = input("Wprowadź nowe dane: ")
            query2 = f'update employees set {field_name}=%s where employee_id =%s'
            data2 = [new_data, employee_idv]
            cursor.execute(query2, data2)
            conn.commit()
            print("Powodzenie!")
        conn.close()