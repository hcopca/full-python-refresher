class Device :
    def __init__ (self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected =  True
    

    #!r se usa para evitar poner comillas y sea mas legible
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnected (self):
        self.disconnected = False
        print("Disconnected.")


# printer =  Device ("Printer", "USB")
# print(printer)
# printer.disconnected()

#Lo que hace esta clase es crear Printer, heredando todo lo de Device
#super está convirtiendo a Printer en superclase
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()}({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printed is not connected")
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)

printer.disconnected()