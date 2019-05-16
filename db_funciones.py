import psycopg2
from psycopg2 import Error

connection = None

try:
    connection = psycopg2.connect( host='localhost', user='postgres', password='CURIE123', dbname='proyecto-2' )
    
    connection.autocommit=False

    print("Connexion a la base de datos exitosa")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error conectandose a la base de datos", error)


def consultar_clientes(nit='', nombre=''): 
    rows = None
    try:
        cursor = connection.cursor()
    
        if nit != '' and nombre == '':
            cursor.execute("""
            SELECT *
            FROM cliente
            WHERE nit LIKE %s;
            """,
            (str(nit) + '%',))
        elif nit == '' and nombre != '':
            cursor.execute("""
            SELECT *
            FROM cliente
            WHERE nombre LIKE %s;
            """,
            ('%' + str(nombre) + '%',))
        elif nit != '' and nombre != '':
            cursor.execute("""
            SELECT *
            FROM cliente
            WHERE nit LIKE %s and nombre LIKE %s;
            """,
            (str(nit) + '%','%' + str(nombre) + '%'))
        else:
            cursor.execute("""
            SELECT *
            FROM cliente;
            """)
        connection.commit()
        rows = cursor.fetchall()
        print(rows)
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error al insertar datos de prueba", error)
        connection.rollback()
    finally:
        if(connection):
            cursor.close()
        return rows