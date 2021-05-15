import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="hr"
)

class Create:
    def create_data_in_jobs(self): #dodawanie danych do tabeli jobs
        print("Podaj wartości pól:")
        job_idv = input('job_id: ')
        job_titlev = input('job_title: ')
        min_salaryv = input('min_salary: ')
        max_salaryv = input('max_salary: ')

        query = "insert into jobs (job_id, job_title, min_salary, max_salary) values(%s, %s, %s, %s)"
        data = (job_idv, job_titlev, min_salaryv, max_salaryv)
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        print('Powodzenie!')

        conn.close()