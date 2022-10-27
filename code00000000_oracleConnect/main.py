import oracledb
import os

username = os.environ.get("PYTHON_USERNAME")
password = os.environ.get("PYTHON_PASSWORD")
connect_string = os.environ.get("PYTHON_CONNECTSTRING")



connection = oracledb.connect(user=username, password=password, dsn=connect_string)

with connection.cursor() as cursor:
    try:

        sql = """select systimestamp from dual"""
        for r in cursor.execute(sql):
            print(r)

    except oracledb.Error as e:
        error, = e.args
        print(error.message)
        print(sql)
        if (error.offset):
            print('^'.rjust(error.offset+1, ' '))