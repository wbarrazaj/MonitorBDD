from clases.cls_Bdd import BaseDD


#database=BaseDD(servidor='Ares2', usuario='root',clave='Emilita01',db='Prueba',puerto='3306',drver='', motor='MariaDB')
#print(database)
#database.ejecutar_query("select 'Hola'")

print("Postgres")

database=BaseDD(servidor='Ares2', usuario='postgres',clave='Emilita01',db='Prueba',puerto='5432',drver='', motor='Postgres')
print(database)
database.ejecutar_query("SELECT version();")
