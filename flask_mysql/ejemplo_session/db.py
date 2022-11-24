import pymysql.cursors
import pprint

def get_users():
    # creamos una conexión a MySQL
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1005',
        database='twitter',
        cursorclass=pymysql.cursors.DictCursor
    )
    # le pido a la conexion un cursor
    cursor = conn.cursor()

    # ejecuto una consulta SQL
    cursor.execute('select * from users')

    results = cursor.fetchall()

    return results

def get_tweets():
    # creamos una conexión a MySQL
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1005',
        database='twitter',
        cursorclass=pymysql.cursors.DictCursor
    )
    # le pido a la conexion un cursor
    cursor = conn.cursor()

    # ejecuto una consulta SQL
    cursor.execute('select * from tweets')

    results = cursor.fetchall()

    return results


if __name__ == '__main__':
    try:
        num1 = 10
        num2 = 5 - 5
        res = num1 / num2
        print(f'El resultado es {res}')
    
    except Exception as ex:
        print(ex)
    
    finally:
        print('Se terminó la operación')
