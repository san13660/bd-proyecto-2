from tkinter import Tk, ttk, messagebox, Menu, END, font # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
import pygubu

class Application(pygubu.TkApplication):
    def _create_ui(self):
        #bold_font = font.Font(weight='bold', size=14)
        self.total = 0

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('test.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('mainwindow', self.master)

        self.tree = builder.get_object('treeview')
        self.entry_nit = builder.get_object('entry_nit')
        self.entry_name = builder.get_object('entry_name')
        self.entry_product = builder.get_object('entry_product')
        self.entry_quantity = builder.get_object('entry_quantity')

        self.label_total = builder.get_object('label_total')

        #self.mainmenu = menu = builder.get_object('mainmenu', self.master)
        #self.set_menu(menu)

        builder.connect_callbacks(self)

    def show_dialog(self):
        print("HOLA")
        messagebox.showinfo("Information","Informative message")

    def insert_row(self):
        product_name = self.entry_product.get()
        quantity = int(self.entry_quantity.get())
        unit_price = 23
        total_price = quantity * unit_price
        self.tree.insert('', END, text=1, values=(quantity,product_name,unit_price,total_price))
        
        self.total += total_price

        self.label_total['text'] = 'Q ' + str(self.total)

    def finish_invoice(self):
        self.tree.delete(*self.tree.get_children())
        self.entry_product.delete(0, END)
        self.entry_quantity.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_nit.delete(0, END)
        self.label_total['text'] = 'Q 0.00'


window = Tk()
app = Application(window)
window.title('Ventas')
window.mainloop()