class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive is None:
            print("Обычная газировка")
        else:
            print ("Газировка с", self.additive)


sodalove = Soda("лимоном")
sodanelove = Soda()
sodalove.show_my_drink()
sodanelove.show_my_drink()
