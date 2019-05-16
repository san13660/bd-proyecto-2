import psycopg2
from psycopg2 import Error

connection = None

try:
    connection = psycopg2.connect( host='localhost', user='postgres', password='basesdedatos', dbname='proyecto-2' )
    
    connection.autocommit=False

    print("Connexion a la base de datos exitosa")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error conectandose a la base de datos", error)


def consultar_clientes(nit='', nombre=''): 
    rows = []
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
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error al leer datos de clientes", error)
        connection.rollback()
    finally:
        if(connection):
            cursor.close()
        return rows


def consultar_productos(id='', nombre='', categoria='', marca=''): 
    rows = []
    try:
        cursor = connection.cursor()
    
        if id != '' and nombre == '' and categoria == '' and marca == '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE id LIKE %s;
            """,
            (str(id) + '%',))
        elif id != '' and nombre != '' and categoria == '' and marca == '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE id LIKE %s and nombre LIKE %s;
            """,
            (str(id) + '%', '%' + str(nombre) + '%',))
        elif id != '' and nombre == '' and categoria != '' and marca == '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE id LIKE %s and categoria LIKE %s;
            """,
            (str(id) + '%', '%' + str(categoria) + '%',))
        elif id != '' and nombre == '' and categoria == '' and marca != '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE id LIKE %s and marca LIKE %s;
            """,
            (str(id) + '%', '%' + str(marca) + '%',))
        elif id != '' and nombre != '' and categoria != '' and marca == '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE id LIKE %s and nombre LIKE %s and categoria LIKE %s;
            """,
            (str(id) + '%', '%' + str(nombre) + '%', '%' + str(categoria) + '%',))
        elif id != '' and nombre == '' and categoria != '' and marca != '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE id LIKE %s and categoria LIKE %s and marca LIKE %s;
            """,
            (str(id) + '%', '%' + str(categoria) + '%', '%' + str(marca) + '%',))
        elif id != '' and nombre != '' and categoria == '' and marca != '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE id LIKE %s and nombre LIKE %s and marca LIKE %s;
            """,
            (str(id) + '%', '%' + str(nombre) + '%', '%' + str(marca) + '%',))
        elif id == '' and nombre != '' and categoria == '' and marca == '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE nombre LIKE %s;
            """,
            ('%' + str(nombre) + '%',))
        elif id == '' and nombre != '' and categoria == '' and marca != '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE nombre LIKE %s and marca LIKE %s;
            """,
            ('%' + str(nombre) + '%', '%' + str(marca) + '%',))
        elif id == '' and nombre != '' and categoria != '' and marca == '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE nombre LIKE %s and categoria LIKE %s;
            """,
            ('%' + str(nombre) + '%', '%' + str(categoria) + '%',))
        elif id == '' and nombre != '' and categoria != '' and marca != '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE nombre LIKE %s and categoria LIKE %s and marca LIKE %s;
            """,
            ('%' + str(nombre) + '%', '%' + str(categoria) + '%', '%' + str(marca) + '%',))
        elif id == '' and nombre == '' and categoria != '' and marca == '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE categoria LIKE %s;
            """,
            ('%' + str(categoria) + '%',))
        elif id == '' and nombre == '' and categoria != '' and marca != '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE categoria LIKE %s and marca LIKE %s;
            """,
            ('%' + str(categoria) + '%', '%' + str(marca) + '%',))
        elif id == '' and nombre == '' and categoria == '' and marca != '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE marca LIKE %s;
            """,
            ('%' + str(marca) + '%',))
        elif id != '' and nombre != '' and categoria != '' and marca != '':
            cursor.execute("""
            SELECT *
            FROM producto
            WHERE id LIKE %s and nombre LIKE %s and categoria LIKE %s and marca LIKE %s;
            """,
            (str(id) + '%', '%' + str(nombre) + '%', '%' + str(categoria) + '%', '%' + str(marca) + '%'))
        else:
            cursor.execute("""
            SELECT *
            FROM producto;
            """)
        connection.commit()
        rows = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error al leer datos de productos", error)
        connection.rollback()
    finally:
        if(connection):
            cursor.close()
        return rows


def ingresar_cliente(nit, nombre): 
    if nit == '' or nombre == '' or len(nit) < 7 or len(nit) > 8:
        return False

    result = False
    try:
        cursor = connection.cursor()
    
        cursor.execute("""
        INSERT INTO cliente(
            nit, nombre
        )
        VALUES(
            %s, %s
        );
        """,
        (str(nit), str(nombre)))
        connection.commit()
        result = True
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error al insertar datos de clientes", error)
        connection.rollback()
    finally:
        if(connection):
            cursor.close()
        return result


def ingresar_factura(nit, fecha, total, lineas_factura): 
    if nit == '' or fecha == '' or total == 0 or len(lineas_factura) == 0:
        return False

    result = False
    try:
        cursor = connection.cursor()
    
        cursor.execute("""
        INSERT INTO factura(
            nit, fecha, total
        )
        VALUES(
            %s, %s, %s
        );
        """,
        (str(nit), str(fecha), str(total)))

        cursor.execute("""
        SELECT id
        FROM factura
        ORDER BY id DESC
        LIMIT 1;
        """)

        row = cursor.fetchone()

        for linea_factura in lineas_factura:
            cursor.execute("""
            INSERT INTO linea_factura(
                id_factura, id_producto, cantidad, sub_total
            )
            VALUES(
                %s, %s, %s, %s
            );
            """,
            (str(row[0]), str(linea_factura[0]), str(linea_factura[1]), str(linea_factura[2])))

        connection.commit()
        
        result = True
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error al insertar factura", error)
        connection.rollback()
    finally:
        if(connection):
            cursor.close()
        return result

def consultar_facturas(id='', nit='', fecha=None): 
    rows = []
    try:
        cursor = connection.cursor()
    
        if id != '' and nit == '' and fecha == None:
            cursor.execute("""
            SELECT *
            FROM factura
            WHERE id LIKE %s;
            """,
            (str(id) + '%',))
        elif id == '' and nit != '' and fecha == None:
            cursor.execute("""
            SELECT *
            FROM factura
            WHERE nit LIKE %s;
            """,
            ('%' + str(nit) + '%',))
        elif id != '' and nit != '' and fecha == None:
            cursor.execute("""
            SELECT *
            FROM factura
            WHERE id LIKE %s and nit LIKE %s;
            """,
            (str(id) + '%', '%' + str(nit) + '%',))
        elif id != '' and nit == '' and fecha != None:
            cursor.execute("""
            SELECT *
            FROM factura
            WHERE id LIKE %s and fecha == %s;
            """,
            (str(id) + '%', str(fecha),))
        elif id == '' and nit != '' and fecha != None:
            cursor.execute("""
            SELECT *
            FROM factura
            WHERE nit LIKE %s and fecha == %s;
            """,
            ('%' + str(nit) + '%', str(fecha),))
        elif id != '' and nit != '' and fecha != None:
            cursor.execute("""
            SELECT *
            FROM factura
            WHERE id LIKE %s and nit LIKE %s and fecha == %s;
            """,
            (str(id) + '%', '%' + str(nit) + '%', str(fecha)))
        else:
            cursor.execute("""
            SELECT *
            FROM factura;
            """)
        connection.commit()
        rows = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error al leer datos de facturas", error)
        connection.rollback()
    finally:
        if(connection):
            cursor.close()
        return rows