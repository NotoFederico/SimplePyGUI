import gi
import webbrowser

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Ventana():
    __builder = None
    __lblLabel = None
    __wndMain = None

    def __init__(self, gladefile):
        builder = Gtk.Builder()
        builder.add_from_file(gladefile)
        builder.connect_signals(self)
        self.__window = builder.get_object("window")
        self.__label = builder.get_object("label1")
        self.counter = 0

    def showWindow(self):
        self.__window.show_all()

    def on_helpButton_clicked(self, button):
        self.__label.set_text("Press OK to go to Mars Site")
        print("Made by Federico Noto")

    def on_okButton_clicked(self, button):
        webbrowser.open("https://mars.nasa.gov/mars2020", new=1)
        print("Going to NASA's Perseverance Site!")

if __name__ == "__main__":
    ventana = Ventana("gui01.glade")
    ventana.showWindow()
    Gtk.main()
