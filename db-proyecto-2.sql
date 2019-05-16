CREATE TABLE cliente (
	nit VARCHAR(10) PRIMARY KEY,
	nombre VARCHAR(30));
	

CREATE TABLE factura (
	id VARCHAR(10) PRIMARY KEY,
	nit VARCHAR(10) REFERENCES cliente(nit),
	fecha DATE,
	total REAL);

CREATE TABLE producto (
	id VARCHAR(10) PRIMARY KEY,
	nombre VARCHAR(20),
	categoria VARCHAR(20),
	marca VARCHAR(20),
	precio REAL);
	

CREATE TABLE linea_factura (
	id VARCHAR(10) PRIMARY KEY,
	id_factura VARCHAR(10) REFERENCES factura(id),
	id_producto VARCHAR(10) REFERENCES producto(id),
	cantidad INTEGER,
	sub_total REAL);

CREATE TABLE tipo_custom (
	nombre VARCHAR(30) PRIMARY KEY,
	tipo VARCHAR(20));
	

CREATE TABLE custom (
	id_producto VARCHAR(20) REFERENCES producto(id),
	nombre_tipo_custom VARCHAR(20) REFERENCES tipo_custom(nombre),
	valor VARCHAR(50),
	PRIMARY KEY (id_producto, nombre_tipo_custom));
	


INSERT INTO cliente(nit, nombre) VALUES('25685987', 'Karla Gonzales');
INSERT INTO cliente(nit, nombre) VALUES('15685845', 'Roberto Gonzales');
INSERT INTO cliente(nit, nombre) VALUES('55661854', 'Florentina Gonzales');
INSERT INTO cliente(nit, nombre) VALUES('57484886', 'Raul Gonzales');
INSERT INTO cliente(nit, nombre) VALUES('88484556', 'Eduardo Gonzales');

INSERT INTO factura(id, nit, fecha, total) VALUES('165184', '25685987', '2019-05-15 11:45:05', 3800.99);
INSERT INTO producto(id, nombre, categoria, marca, precio) VALUES('1561851', 'Lavadora', 'Linea Blanca', 'LG', 3000.00);
INSERT INTO producto(id, nombre, categoria, marca, precio) VALUES('1561895', 'Microondas', 'Linea Blanca', 'Whirlpool', 800.99);
INSERT INTO linea_factura(id, id_factura, id_producto, cantidad, sub_total) VALUES('551651', '165184', '1561851', 1, 3000.00);
INSERT INTO linea_factura(id, id_factura, id_producto, cantidad, sub_total) VALUES('551652', '165184', '1561895', 1, 800.99);

INSERT INTO tipo_custom(nombre, tipo) VALUES('color', 'string');
INSERT INTO tipo_custom(nombre, tipo) VALUES('peso', 'float');
INSERT INTO custom(id_producto, nombre_tipo_custom, valor) VALUES('1561851', 'color', 'blanco');
INSERT INTO custom(id_producto, nombre_tipo_custom, valor) VALUES('1561895', 'color', 'negro');

INSERT INTO custom(id_producto, nombre_tipo_custom, valor) VALUES('1561851', 'peso', '100.00');
INSERT INTO custom(id_producto, nombre_tipo_custom, valor) VALUES('1561895', 'peso', '10.00');



SELECT producto.id, nombre, categoria, marca, precio,
array_agg(custom.nombre_tipo_custom) AS custom_categorias, array_agg(custom.valor) AS custom_valores 
FROM producto JOIN custom ON custom.id_producto = producto.id 
GROUP BY producto.id;