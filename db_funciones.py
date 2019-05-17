import psycopg2
from psycopg2 import Error
from faker import Faker
import random

fake = Faker()

connection = None

try:
    connection = psycopg2.connect( host='localhost', user='postgres', password='CURIE123', dbname='proyecto-2' )
    
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

def consultar_customs(): 
    rows = []
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT *
        FROM tipo_custom;
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
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id 
            WHERE id LIKE %s
            GROUP BY producto.id;
            """,
            (str(id) + '%',))
        elif id != '' and nombre != '' and categoria == '' and marca == '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE id LIKE %s and nombre LIKE %s
            GROUP BY producto.id;
            """,
            (str(id) + '%', '%' + str(nombre) + '%',))
        elif id != '' and nombre == '' and categoria != '' and marca == '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE id LIKE %s and categoria LIKE %s
            GROUP BY producto.id;
            """,
            (str(id) + '%', '%' + str(categoria) + '%',))
        elif id != '' and nombre == '' and categoria == '' and marca != '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE id LIKE %s and marca LIKE %s
            GROUP BY producto.id;
            """,
            (str(id) + '%', '%' + str(marca) + '%',))
        elif id != '' and nombre != '' and categoria != '' and marca == '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE id LIKE %s and nombre LIKE %s and categoria LIKE %s
            GROUP BY producto.id;
            """,
            (str(id) + '%', '%' + str(nombre) + '%', '%' + str(categoria) + '%',))
        elif id != '' and nombre == '' and categoria != '' and marca != '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE id LIKE %s and categoria LIKE %s and marca LIKE %s
            GROUP BY producto.id;
            """,
            (str(id) + '%', '%' + str(categoria) + '%', '%' + str(marca) + '%',))
        elif id != '' and nombre != '' and categoria == '' and marca != '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE id LIKE %s and nombre LIKE %s and marca LIKE %s
            GROUP BY producto.id;
            """,
            (str(id) + '%', '%' + str(nombre) + '%', '%' + str(marca) + '%',))
        elif id == '' and nombre != '' and categoria == '' and marca == '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE nombre LIKE %s
            GROUP BY producto.id;
            """,
            ('%' + str(nombre) + '%',))
        elif id == '' and nombre != '' and categoria == '' and marca != '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE nombre LIKE %s and marca LIKE %s
            GROUP BY producto.id;
            """,
            ('%' + str(nombre) + '%', '%' + str(marca) + '%',))
        elif id == '' and nombre != '' and categoria != '' and marca == '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE nombre LIKE %s and categoria LIKE %s
            GROUP BY producto.id;
            """,
            ('%' + str(nombre) + '%', '%' + str(categoria) + '%',))
        elif id == '' and nombre != '' and categoria != '' and marca != '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE nombre LIKE %s and categoria LIKE %s and marca LIKE %s
            GROUP BY producto.id;
            """,
            ('%' + str(nombre) + '%', '%' + str(categoria) + '%', '%' + str(marca) + '%',))
        elif id == '' and nombre == '' and categoria != '' and marca == '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE categoria LIKE %s
            GROUP BY producto.id;
            """,
            ('%' + str(categoria) + '%',))
        elif id == '' and nombre == '' and categoria != '' and marca != '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE categoria LIKE %s and marca LIKE %s
            GROUP BY producto.id;
            """,
            ('%' + str(categoria) + '%', '%' + str(marca) + '%',))
        elif id == '' and nombre == '' and categoria == '' and marca != '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE marca LIKE %s
            GROUP BY producto.id;
            """,
            ('%' + str(marca) + '%',))
        elif id != '' and nombre != '' and categoria != '' and marca != '':
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            WHERE id LIKE %s and nombre LIKE %s and categoria LIKE %s and marca LIKE %s
            GROUP BY producto.id;
            """,
            (str(id) + '%', '%' + str(nombre) + '%', '%' + str(categoria) + '%', '%' + str(marca) + '%'))
        else:
            cursor.execute("""
            SELECT producto.id, nombre, categoria, marca, precio,
            array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
            FROM producto JOIN custom ON custom.id_producto = producto.id
            GROUP BY producto.id;
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


def ingresar_custom(nombre, tipo): 
    if nombre == '' or tipo == '':
        return False

    result = False
    try:
        cursor = connection.cursor()
    
        cursor.execute("""
        INSERT INTO tipo_custom(
            nombre, tipo
        )
        VALUES(
            %s, %s
        );
        """,
        (str(nombre), str(tipo)))
        connection.commit()
        result = True
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error al insertar datos de custom", error)
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

def consultar_facturas(id='', nit='', fecha=''): 
    rows = []
    try:
        cursor = connection.cursor()
    
        if id != '' and nit == '' and fecha == '':
            cursor.execute("""
            SELECT id, factura.nit, nombre, fecha, total 
            FROM factura
            JOIN cliente ON factura.nit = cliente.nit
            WHERE id LIKE %s;
            """,
            (str(id) + '%',))
        elif id == '' and nit != '' and fecha == '':
            cursor.execute("""
            SELECT id, factura.nit, nombre, fecha, total 
            FROM factura
            JOIN cliente ON factura.nit = cliente.nit
            WHERE factura.nit LIKE %s;
            """,
            ('%' + str(nit) + '%',))
        elif id == '' and nit == '' and fecha != '':
            cursor.execute("""
            SELECT id, factura.nit, nombre, fecha, total 
            FROM factura
            JOIN cliente ON factura.nit = cliente.nit
            WHERE fecha = %s;
            """,
            (str(fecha),))
        elif id != '' and nit != '' and fecha == '':
            cursor.execute("""
            SELECT id, factura.nit, nombre, fecha, total 
            FROM factura
            JOIN cliente ON factura.nit = cliente.nit
            WHERE id LIKE %s and factura.nit LIKE %s;
            """,
            (str(id) + '%', '%' + str(nit) + '%',))
        elif id != '' and nit == '' and fecha != '':
            cursor.execute("""
            SELECT id, factura.nit, nombre, fecha, total 
            FROM factura
            JOIN cliente ON factura.nit = cliente.nit
            WHERE id LIKE %s and fecha == %s;
            """,
            (str(id) + '%', str(fecha),))
        elif id == '' and nit != '' and fecha != '':
            cursor.execute("""
            SELECT id, factura.nit, nombre, fecha, total 
            FROM factura
            JOIN cliente ON factura.nit = cliente.nit
            WHERE factura.nit LIKE %s and fecha == %s;
            """,
            ('%' + str(nit) + '%', str(fecha),))
        elif id != '' and nit != '' and fecha != '':
            cursor.execute("""
            SELECT id, factura.nit, nombre, fecha, total 
            FROM factura
            JOIN cliente ON factura.nit = cliente.nit
            WHERE id LIKE %s and factura.nit LIKE %s and fecha == %s;
            """,
            (str(id) + '%', '%' + str(nit) + '%', str(fecha)))
        else:
            cursor.execute("""
            SELECT id, factura.nit, nombre, fecha, total 
            FROM factura
            JOIN cliente ON factura.nit = cliente.nit;
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

def fakeins():
    cur = connection.cursor()
    productos=["leche","queso", "yougurt","crema","helado","pollo","res","cerdo","pescado","cereales","arroz","trigo","harina","maiz","cloro","jabon","jabon en polvo","desinfectante","detergentes","suavisantes","papel higienico"]
    categorias =["lacteos","lacteos","lacteos","lacteos","lacteos","carne","carne","carne","carne","granos","granos","granos","granos","granos","limpieza","limpieza","limpieza","limpieza","limpieza","limpieza","limpieza"]
    for x in range(0, 20):
        print(fake.company())
        cur.execute("INSERT INTO producto(id, nombre, categoria, marca, precio) VALUES('" + str(random.randint(100,100000))+ "', '" + productos[x] +"', '"+ categorias[x]+"', '"+ fake.company()+"',"+ str(round(random.uniform(15.0,50.0), 2))+");")
    connection.commit()


def createFD(fecha_base):
    cur = connection.cursor()
    try:
        cur.execute("SELECT id FROM factura ORDER BY id DESC LIMIT 1")
        id_fac = cur.fetchall()
        cas = id_fac[0][0]
    except:
        cas = 0
    cur.execute("SELECT * FROM producto")
    rows = cur.fetchall()
    ventas = random.randint(100,200)
    for x in range(0,ventas):
        nit = random.randint(10000000,99999999)
        nombre = fake.name()
        cur.execute("INSERT INTO cliente(nit, nombre) VALUES('"+ str(nit)+"', '" + str(nombre) +"');")
        cont = random.randint(1,2)
        for y in range(0,cont-1):
            fecha = fecha_base + " " + fake.time_object(end_datetime=None).strftime("%H:%M:%S")
            cas += 1
            total = 0.0
            cor = random.randint(5,20)
            lineas = []
            for z in range(0,cor):
                cant = random.randint(1,5)
                m = random.randint(0,19)
                sub_total = float(rows[m][4])*cant
                total += sub_total
                lineas.append("INSERT INTO linea_factura(id_factura, id_producto, cantidad, sub_total) VALUES('"+ str(cas)+"', '"+ rows[m][0] +"', "+ str(cant)+", "+ str(sub_total)+");")
                

            cur.execute("INSERT INTO factura(nit, fecha, total) VALUES('"+ str(nit) +"', '"+ str(fecha)+"', "+ str(total)+");")
            connection.commit()
            for w in range(0,len(lineas)):
                cur.execute(lineas[w])
            connection.commit()