#import sqlanydb
import os
import pyodbc

from clases.cls_Bdd import BaseDD

#os.environ["SQLANY_API_DLL"]='/opt/sqlanywhere17/lib64/libdbcapi_r.so'

servidor='193.168.1.175'
usuario='sa' 
clave='Emilita01'
db='master' 
puerto=5000
#drver='Adaptive Server Enterprise'
#drver='/usr/lib/x86_64-linux-gnu/libodbc.so'
drver='/opt/sap/DataAccess64/ODBC/lib/libsybdrvodb.so'
#drver='Sybase ASE ODBC Driver'
#drver='FreeTDS'


Conn = BaseDD(servidor,usuario,clave,db,puerto,drver)


print(Conn.ServidorDB)
print(Conn.UsuarioDB)
print(Conn.SchemaDBD)
print(Conn.Port)
print(Conn.Driver)

a=pyodbc.drivers()
print(a)
print(Conn)


conn = pyodbc.connect(driver=drver, server=servidor , database=db , port=puerto , uid=usuario , pwd=clave , Trusted_Connection='yes')

print("Aqui")

#b=conn.conectar()

#print(b)
print("Termino")
