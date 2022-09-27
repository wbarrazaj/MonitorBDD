import pyodbc 
import pymysql


class BaseDD():
    """
    Server class de Conexion.
    __conectar    : metodo de conexion.
    """
    def __init__(self, servidor, usuario, clave, db, puerto, drver , motor ):
        self.ServidorDB = servidor 
        self.UsuarioDB =  usuario
        self.PasswordDB = clave
        self.SchemaDBD = db
        self.Port = puerto 
        self.Driver = drver
        self.Motor = motor
    
    def conectar(self):
        if self.Motor == 'Sybase': 
            conn = pyodbc.connect(
                                    driver=self.Driver, 
                                    server=self.ServidorDB , 
                                    database=self.SchemaDBD ,
                                    port = self.Port,
                                    uid=self.UsuarioDB, 
                                    pwd=self.PasswordDB
                                    )
        elif self.Motor in ('Mysql','MariaDB'):
            conn = pymysql.connect(
                                    host=self.ServidorDB,
                                    user=self.UsuarioDB,
                                    password=self.PasswordDB,
                                    db=self.SchemaDBD
                                    ) 

            print("MYSQL")
        return conn

    def ejecutar_query(self, query):
        conn=self.conectar()
        print(self.Motor)
        if self.Motor == 'Sybase':
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            conn.close()
            print("Ejecucion Sybase")
        elif self.Motor in ('Mysql','MariaDB'):
            print('Aqui 1')
            cursor = conn.cursor()
            print('Aqui 2')
            cursor.execute(query)
            resultado=cursor.fetchone()
            print(resultado)
            conn.commit()
            conn.close()
            print("Ejecucion Mysql - MariaDB")
        else:
            print("Otra Motor")

    def chk_default(c):
        res = True
        try:
            c.query('select 1')
            c.use_result()
        except:
            res = False
            
        return res


