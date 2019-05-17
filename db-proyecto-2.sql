CREATE TABLE cliente (
	nit VARCHAR(10) PRIMARY KEY,
	nombre VARCHAR(50));
	

CREATE TABLE factura (
	id SERIAL PRIMARY KEY,
	nit VARCHAR(20) REFERENCES cliente(nit),
	fecha TIMESTAMP,
	total REAL);

CREATE TABLE producto (
	id VARCHAR(20) PRIMARY KEY,
	nombre VARCHAR(30),
	categoria VARCHAR(30),
	marca VARCHAR(50),
	precio REAL);
	

CREATE TABLE linea_factura (
	id SERIAL PRIMARY KEY,
	id_factura INTEGER REFERENCES factura(id),
	id_producto VARCHAR(20) REFERENCES producto(id),
	cantidad INTEGER,
	sub_total REAL);

CREATE TABLE tipo_custom (
	nombre VARCHAR(30) PRIMARY KEY,
	tipo VARCHAR(30));
	

CREATE TABLE custom (
	id_producto VARCHAR(30) REFERENCES producto(id),
	nombre_tipo_custom VARCHAR(30) REFERENCES tipo_custom(nombre),
	valor VARCHAR(50),
	PRIMARY KEY (id_producto, nombre_tipo_custom));
	


INSERT INTO cliente(nit, nombre) VALUES('25685987', 'Karla Gonzales');
INSERT INTO cliente(nit, nombre) VALUES('15685845', 'Roberto Gonzales');
INSERT INTO cliente(nit, nombre) VALUES('55661854', 'Florentina Gonzales');
INSERT INTO cliente(nit, nombre) VALUES('57484886', 'Raul Gonzales');
INSERT INTO cliente(nit, nombre) VALUES('88484556', 'Eduardo Gonzales');

INSERT INTO factura(nit, fecha, total) VALUES('25685987', '2019-05-15 11:45:05', 3800.99);
INSERT INTO producto(id, nombre, categoria, marca, precio) VALUES('1561851', 'Lavadora', 'Linea Blanca', 'LG', 3000.00);
INSERT INTO producto(id, nombre, categoria, marca, precio) VALUES('1561895', 'Microondas', 'Linea Blanca', 'Whirlpool', 800.99);
INSERT INTO linea_factura(id_factura, id_producto, cantidad, sub_total) VALUES('1', '1561851', 1, 3000.00);
INSERT INTO linea_factura(id_factura, id_producto, cantidad, sub_total) VALUES('1', '1561895', 1, 800.99);

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