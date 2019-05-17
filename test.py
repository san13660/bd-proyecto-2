from PyQt5 import uic, QtWidgets
import sys
from db_funciones import *
import datetime

class Ui(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Ventas.ui', self)
        self.pb_facturacion_ingresar.clicked.connect(self.click_ingresar_lineafactura)
        self.pb_facturacion_facturar.clicked.connect(self.click_ingresar_factura)
        self.pb_facturacion_cancelar.clicked.connect(self.click_cancelar_factura)
        self.le_facturacion_nit.returnPressed.connect(self.enter_nit)
        self.le_facturacion_nombre.returnPressed.connect(self.enter_nombre)
        self.le_facturacion_idproducto.returnPressed.connect(self.enter_id_producto)
        self.le_facturacion_cantidad.returnPressed.connect(self.click_ingresar_lineafactura)

        self.pb_historialventas_buscar.clicked.connect(self.click_buscar_facturas)
        
        self.pb_clientes_buscar.clicked.connect(self.click_buscar_clientes)
        self.pb_clientes_ingresar.clicked.connect(self.click_ingresar_cliente)
        self.pb_productos_buscar.clicked.connect(self.click_buscar_productos)
        
        self.total = 0.0
        self.lineas_factura = []

        self.show()
    

    def click_ingresar_lineafactura(self): 
        if self.le_facturacion_idproducto.text() != '':
            producto = consultar_productos(self.le_facturacion_idproducto.text())
            cantidad = self.le_facturacion_cantidad.text()
            if cantidad == '':
                cantidad = '1'
            subtotal = '{0:.2f}'.format((producto[0][4]) * int(cantidad))
            rowPosition = self.tw_facturacion.rowCount()
            self.tw_facturacion.insertRow(rowPosition)
            self.tw_facturacion.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(producto[0][0]))
            self.tw_facturacion.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(producto[0][1]))
            self.tw_facturacion.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(producto[0][4])))
            self.tw_facturacion.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(cantidad))
            self.tw_facturacion.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(str(subtotal)))
            self.total += float(subtotal)
            self.lbl_facturacion_total.setText('Q ' + str(self.total))

            self.lineas_factura.append((producto[0][0], cantidad, subtotal))

            self.le_facturacion_cantidad.setDisabled(True)
            self.le_facturacion_cantidad.setText('1')
            self.le_facturacion_idproducto.setText('')
            self.le_facturacion_idproducto.setFocus()

    def click_ingresar_factura(self):
        if ingresar_factura(self.le_facturacion_nit.text(), datetime.date.today().strftime("%Y-%m-%d %H:%M:%S"), self.total, self.lineas_factura):

            self.le_facturacion_nit.setText('')
            self.le_facturacion_nombre.setText('')
            self.le_facturacion_idproducto.setText('')
            self.le_facturacion_cantidad.setText('1')

            self.le_facturacion_nit.setDisabled(False)
            self.le_facturacion_nombre.setDisabled(True)
            self.le_facturacion_idproducto.setDisabled(True)
            self.le_facturacion_cantidad.setDisabled(True)

            self.tw_facturacion.setRowCount(0)

            self.total = 0
            self.lineas_factura = []
            self.lbl_facturacion_total.setText('Q 0.00')

            self.le_facturacion_nit.setFocus()

    def click_cancelar_factura(self):
        self.le_facturacion_nit.setText('')
        self.le_facturacion_nombre.setText('')
        self.le_facturacion_idproducto.setText('')
        self.le_facturacion_cantidad.setText('1')

        self.le_facturacion_nit.setDisabled(False)
        self.le_facturacion_nombre.setDisabled(True)
        self.le_facturacion_idproducto.setDisabled(True)
        self.le_facturacion_cantidad.setDisabled(True)

        self.tw_facturacion.setRowCount(0)

        self.total = 0
        self.lineas_factura = []
        self.lbl_facturacion_total.setText('Q 0.00')

        self.le_facturacion_nit.setFocus()

    def click_buscar_clientes(self):
        rows = consultar_clientes(self.le_clientes_nit.text(), self.le_clientes_nombre.text())
        self.tw_clientes.setRowCount(0)
        for row in rows:
            rowPosition = self.tw_clientes.rowCount()
            self.tw_clientes.insertRow(rowPosition)
            self.tw_clientes.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tw_clientes.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(row[1]))

    def enter_nit(self):
        if self.le_facturacion_nit != '':
            rows = consultar_clientes(self.le_facturacion_nit.text(), '')
            if len(rows) > 0:
                self.le_facturacion_nit.setText(rows[0][0])
                self.le_facturacion_nombre.setText(rows[0][1])
                self.le_facturacion_nit.setDisabled(True)
                self.le_facturacion_idproducto.setDisabled(False)
                self.le_facturacion_idproducto.setFocus()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("El nit ingresado no existe. Por favor ingrese el nombre para crear un nuevo cliente.")
                msg.setWindowTitle("Nit no registrado")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
                self.le_facturacion_nombre.setDisabled(False)
                self.le_facturacion_nombre.setFocus()

    def enter_nombre(self):
        if self.le_facturacion_nombre != '':
            if ingresar_cliente(self.le_facturacion_nit.text(), self.le_facturacion_nombre.text()):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Cliente ingresado correctamente.")
                msg.setWindowTitle("Nuevo cliente registrado")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
                self.le_facturacion_nit.setDisabled(True)
                self.le_facturacion_nombre.setDisabled(True)
                self.le_facturacion_idproducto.setDisabled(False)
                self.le_facturacion_cantidad.setText('1')
                self.le_facturacion_idproducto.setFocus()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Error al ingresar cliente. Intente nuevamente")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()


    def enter_id_producto(self):
        if self.le_facturacion_idproducto != '':
            rows = consultar_productos(self.le_facturacion_idproducto.text())
            if len(rows) > 0:
                self.le_facturacion_cantidad.setText('1')
                self.le_facturacion_cantidad.setDisabled(False)
                self.le_facturacion_cantidad.setFocus()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("No se encontro el id de producto. Intente nuevamente")
                msg.setWindowTitle("ID de producto")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()   
    

    def click_buscar_productos(self):
        rows = consultar_productos(self.le_productos_id.text(), self.le_productos_nombre.text(), self.le_productos_categoria.text(), self.le_productos_marca.text())
        self.tw_productos.setRowCount(0)
        for row in rows:
            rowPosition = self.tw_productos.rowCount()
            self.tw_productos.insertRow(rowPosition)
            self.tw_productos.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tw_productos.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tw_productos.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tw_productos.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tw_productos.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(str(row[4])))


    def click_ingresar_cliente(self):
        msg = QtWidgets.QMessageBox()
        if ingresar_cliente(self.le_clientes_nit.text(), self.le_clientes_nombre.text()):
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Cliente ingresado exitosamente.")
            msg.setWindowTitle("Ingreso de cliente")
        else:
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error al ingresar cliente.")
            msg.setWindowTitle("Ingreso de cliente")   
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def click_buscar_facturas(self):
        fecha = ''
        if self.cb_historialventas_fecha.isChecked():
            fecha = self.de_historialventas_fecha.date().toPyDate().strftime("%Y-%m-%d %H:%M:%S")
        
        print(fecha)
        rows = consultar_facturas(self.le_historialventas_id.text(), self.le_historialventas_nit.text(), fecha)
        
        self.tw_historialventas.setRowCount(0)
        for row in rows:
            rowPosition = self.tw_historialventas.rowCount()
            self.tw_historialventas.insertRow(rowPosition)
            self.tw_historialventas.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tw_historialventas.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tw_historialventas.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tw_historialventas.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(str(row[3].strftime("%Y-%m-%d %H:%M:%S"))))
            self.tw_historialventas.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(str(row[4])))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())