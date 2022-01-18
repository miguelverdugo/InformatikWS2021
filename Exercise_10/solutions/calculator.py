import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    clear = False
    numstr = ""
    numopstr = ""
    entry = Gtk.Entry()

    def __init__(self):
        Gtk.Window.__init__(self, title="Taschenrechner")

        table = Gtk.Table(n_rows=5,n_columns=4,homogeneous=True)

        table.attach(self.entry,0,4,0,1)

        # operations
        for i,op in enumerate(["+", "-", "*", "/"]):
            op_button = Gtk.Button(label=op)
            table.attach(op_button,3,4,i+1,i+2)
        # numbers
        for n in range(10):
            num_button = Gtk.Button(label=str(n))
            if n == 0:
                pos = (1,2,4,5)
            else:
                pos = ((n-1)%3,(n-1)%3+1,(n-1)//3+1,(n-1)//3+2)
            table.attach(num_button,*pos)
            
        # floating point button
        point_button = Gtk.Button(label=".")
        table.attach(point_button,0,1,4,5)


        self.add(table)






window = MyWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
