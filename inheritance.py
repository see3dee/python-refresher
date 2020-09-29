class Device:
    def __init__(self, name, connection_type):
        self.name = name
        self.connection_type = connection_type
        self.connected = True

    def __str__(self):
        return f"This Device is a {self.name!r} that connects with {self.connection_type}"


    def disconnect(self):
        print(f"The Device: {self.name!r} is being disconnected")
        self.connected = False
        print(f"The Device: {self.name!r} is no longer connected")


printer = Device('Printer', 'USB')
print(printer)
printer.disconnect()


#  Using and expanding a parent class
#  Instead of duplicating all the parent class init's - initiate the 'super().__init__() == Device().__init__()' and
#  then add the new inits to the class, as usual
class Printer(Device):
    def __init__(self, name, connection_type, capacity):
        super().__init__(name, connection_type)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages}) pages remaining"

    def print(self, pages):
        if not self.connected:
            print('Your device is not connected, please connect and try again.')
            return
        print(f'Printing {self.remaining_pages} pages.')
        self.remaining_pages -= pages


hp = Printer("laser", 'ethernet', 600)

print(hp)
hp.print(300)
print(hp)
hp.disconnect()
hp.print(30)





