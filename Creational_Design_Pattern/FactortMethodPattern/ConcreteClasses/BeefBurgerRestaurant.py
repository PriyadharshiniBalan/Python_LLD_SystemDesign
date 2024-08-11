from Interface.Restaurant import Restaurant
from Interface.IBurger import IBurger
from Products.BeefBurger import BeefBurger

class BeefBurgerRestaurant(Restaurant):
    
    def createBurger(self) -> IBurger:
        return BeefBurger()