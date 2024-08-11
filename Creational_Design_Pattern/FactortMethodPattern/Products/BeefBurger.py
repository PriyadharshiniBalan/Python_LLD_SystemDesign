from Interface.IBurger import IBurger

class BeefBurger(IBurger):

    def prepare(self):
        print("Preparing Beef Burger")
