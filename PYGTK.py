import pygtk
pygtk.require('2.0')
import gtk
import serial

class Base:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.ventana = gtk.VBox()
        var = serial.Serial('/dev/ttyACM0', 9600)
        self.ba = gtk.Button("Encender LED")
        self.bb = gtk.Button("Apagar LED")
        self.bc = gtk.Button("Flash LED")
        self.window.add(self.ventana)
        self.ventana.add(self.ba)
        self.ventana.add(self.bb)
        self.ventana.add(self.bc)
    	self.ventana.show_all()
        self.window.show_all()

        def vara(self):
        	var.write('a')
        self.ba.connect('clicked',vara)

        def varb(self):
        	var.write('b')
        self.bb.connect('clicked',varb)

        def varc(self):
        	var.write('c')
        self.bc.connect('clicked',varc)


    def main(self):
        gtk.main()

print __name__
if __name__ == "__main__":
    base = Base()
    base.main()
