from abc import ABC, abstractmethod
from Interface.IBurger import IBurger

class Restaurant(ABC):
    def orderBurger(self):
        burger = self.createBurger()
        burger.prepare()
        return burger

    def createBurger(self) -> IBurger:
        pass