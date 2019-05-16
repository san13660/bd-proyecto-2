from PyQt5 import uic, QtWidgets
import sys
from db_funciones import *

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Ventas.ui', self)
        self.pb_clientes_buscar.clicked.connect(self.click_buscar_clientes)
        self.show()

    def click_buscar_clientes(self):
        rows = consultar_clientes(self.le_clientes_nit.text(), self.le_clientes_nombre.text())
        self.tw_clientes.setRowCount(0)
        for row in rows:
            rowPosition = self.tw_clientes.rowCount()
            self.tw_clientes.insertRow(rowPosition)
            self.tw_clientes.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tw_clientes.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(row[1]))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())