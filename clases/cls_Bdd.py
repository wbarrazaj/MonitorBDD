import pyodbc 

class BaseDD():
    """
    Server class de Conexion.
    __conectar    : metodo de conexion.
    """
    def __init__(self, servidor, usuario, clave, db, puerto, drver ):
        self.ServidorDB = servidor 
        self.UsuarioDB =  usuario
        self.PasswordDB = clave
        self.SchemaDBD = db
        self.Port = puerto 
        self.Driver = drver
    
    def conectar(self):
        conn = pyodbc.connect(
                                driver=self.Driver, 
                                server=self.ServidorDB , 
                                database=self.SchemaDBD ,
                                port = self.Port,
                                uid=self.UsuarioDB, 
                                pwd=self.PasswordDB
                              )
        return conn

    def ejecutar_query(self, query):
        conn=self.__conectar()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

    def chk_default(c):
        res = True
        try:
            c.query('select 1')
            c.use_result()
        except:
            res = False
            
        return res

