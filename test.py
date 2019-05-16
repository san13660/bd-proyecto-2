from PyQt5 import uic, QtWidgets
import sys
from db_funciones import *

class Ui(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Ventas.ui', self)
        self.pb_facturacion_ingresar.clicked.connect(self.click_ingresar_lineafactura)
        #self.pb_facturacion_facturar.clicked.connect(self.click_ingresar_factura)
        self.pb_clientes_buscar.clicked.connect(self.click_buscar_clientes)
        self.pb_clientes_ingresar.clicked.connect(self.click_ingresar_cliente)
        self.pb_productos_buscar.clicked.connect(self.click_buscar_productos)
        self.total = 0.0
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


    def click_buscar_clientes(self):
        rows = consultar_clientes(self.le_clientes_nit.text(), self.le_clientes_nombre.text())
        self.tw_clientes.setRowCount(0)
        for row in rows:
            rowPosition = self.tw_clientes.rowCount()
            self.tw_clientes.insertRow(rowPosition)
            self.tw_clientes.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tw_clientes.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(row[1]))
    

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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())