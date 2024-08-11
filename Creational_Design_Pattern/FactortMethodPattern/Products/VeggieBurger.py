from Interface.IBurger import IBurger

class VeggieBurger(IBurger):

    def prepare(self):
        print("Preparing Veg Burger")
