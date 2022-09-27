from select import select
import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='Ares2',
            user='root',
            password='Emilita01',
            port=3306,
            db='Prueba'
        )
        self.cursor = self.connection.cursor()
        print("Conexion Establecida")
    def select_user(self,id):
        sql='select id, username, email from users where id={}'.format(id)
        try:
            self.cursor.execute(sql)
            user=self.cursor.fetchone()
            print("Id:", user[0])
            print("Username:", user[1])
            print("Email:", user[2])
        except Exception as e:
            raise

database=DataBase()
database.select_user('1')

