#!/usr/bin/python

import psycopg2
from faker import Faker
import random

fake = Faker()

#connect to the db
con = psycopg2.connect(
    host = "localhost",
    database = "p2p",
    user = "postgres",
    password = "")
#cursor
cur = con.cursor()
productos=["leche","queso", "yougurt","crema","helado","pollo","res","cerdo","pescado","cereales","arroz","trigo","harina","maiz","cloro","jabon","jabon en polvo","desinfectante","detergentes","suavisantes","papel higienico"]
categorias =["lacteos","lacteos","lacteos","lacteos","lacteos","carne","carne","carne","carne","granos","granos","granos","granos","granos","limpieza","limpieza","limpieza","limpieza","limpieza","limpieza","limpieza"]
print(len(productos))
print(len(categorias))
def fakeins():
    
    for x in range(0, 20):
        print(fake.company())
        cur.execute("INSERT INTO producto(id, nombre, categoria, marca, precio) VALUES('" + str(random.randint(100,100000))+ "', '" + productos[x] +"', '"+ categorias[x]+"', '"+ fake.company()+"',"+ str(round(random.uniform(15.0,50.0), 2))+");")
    con.commit()


def createFD():
    try:
        cur.execute("SELECT id FROM factura ORDER BY id DESC LIMIT 1")
        id_fac = cur.fetchall()
        cas = id_fac[0][0]
    except:
        cas = 0
    cur.execute("SELECT * FROM producto"  )
    rows = cur.fetchall()
    fecha = fake.date(pattern="%d-%m-%Y", end_datetime=None)
    ventas = random.randint(300,10000)
    for x in range(0,ventas):
        nit = random.randint(10000000,99999999)
        nombre = fake.name()
        cur.execute("INSERT INTO cliente(nit, nombre) VALUES('"+ str(nit)+"', '" + str(nombre) +"');")
        cont = random.randint(1,2)
        for y in range(0,cont-1):
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
            con.commit()
            for w in range(0,len(lineas)):
                cur.execute(lineas[w])
            con.commit()
            
fakeins()
createFD()


#print(rows[0])
#close the cur
cur.close()
#close the connection
con.close()
