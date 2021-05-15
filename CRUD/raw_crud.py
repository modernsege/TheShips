import mysql.connector
import sys
# ==============================================================FUNCTIONS!============================================================


def connection_to_server(hostAddres='localhost', datab="world"):
    username = input("Please log in to database, input your username: ")
    password = input("Input your password: ")
    #datab = input("Input database you want to use")

    try:
        connector = mysql.connector.connect(
            host=hostAddres, user=username, passwd=password, database=datab)

        return connector
    except:
        print("Nope, access DENIED! ", sys.exc_info()[0])
        return None


def no_easy_insertion(*check_string):
    is_contained = False
    try:
        for i in check_string:
            if i.find(";") != -1:
                is_contained = True
    except:
        pass
    return is_contained


def insert_record(connection, table, values):
    if no_easy_insertion(table, values) == False:
        cursor = connection.cursor()
        try:
            cursor.execute(f"insert into {table} values ({values})")
            connection.commit()
            print("Success!")
        except:
            connection.rollback()
            print("Didnt work. Maybe wrong input. ", sys.exc_info()[0])

    else:
        print("Nice try")


def display_sth(connection, table, columns="*", where_or_having="", group_by=None):
    if no_easy_insertion(table, columns, where_or_having, group_by) == False:
        cursor = connection.cursor()
        if group_by == None:
            try:
                cursor.execute(
                    f"select {columns} from {table} where {where_or_having}")

            except:
                print("Something went HORRIBLY wrong!(where). ",
                      sys.exc_info()[0])
                return None
        else:
            try:
                cursor.execute(
                    f"select {columns} from {table} group by {group_by} having {where_or_having}")

            except:
                print(
                    "Something went HORRIBLY wrong!(group by ... having). ", sys.exc_info()[0])
                return None
        result = cursor.fetchall()

        print(result)
        return result

    else:
        print("Nice try")
        return None


def update_sth(connection, table, change, where):
    if no_easy_insertion(table, change, where) == False:
        cursor = connection.cursor()
        try:
            cursor.execute(f"update {table} set {change} where {where}")
            connection.commit()
            print("Done!")
        except:
            connection.rollback()
            print("It didnt work, but.. You can try again! ",
                  sys.exc_info()[0])
    else:
        print("Nice try")


def delete_sth(connection, table, where):
    if no_easy_insertion(table, where) == False:
        cursor = connection.cursor()
        try:
            cursor.execute(f"delete from {table} where {where}")
            connection.commit()
            print("Jobs done!")
        except:
            connection.rollback()
            print(
                "Well, nope, sorry - sth wrong... Better luck next time. ", sys.exc_info()[0])
    else:
        print("Nice try")

