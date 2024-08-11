from ConcreteClasses.BeefBurgerRestaurant import BeefBurgerRestaurant
from ConcreteClasses.VeggieBurgerRestaurant import VeggieBurgerRestaurant

def main():
    beefResto = BeefBurgerRestaurant()
    beefBurger = beefResto.orderBurger()

    vegResto = VeggieBurgerRestaurant()
    vegBurger = vegResto.orderBurger()


if __name__ == "__main__":
    main()