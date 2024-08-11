from Interface.Restaurant import Restaurant
from Interface.IBurger import IBurger
from Products.VeggieBurger import VeggieBurger

class VeggieBurgerRestaurant(Restaurant):

    def createBurger(self) -> IBurger:
        return VeggieBurger()