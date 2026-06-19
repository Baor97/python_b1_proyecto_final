from abc import ABC, abstractmethod
from .food_package import FoodPackage, Wrapping, Bottle

class Product(ABC):
    def __init__(self,id:str,name:str,price:float):
      self.id = id
      self.name = name
      self.price = price

    def describe(self):
        package = self.foodPackage()
        return (
            f"Product - Type: {self.type()}, Name:{self.name}, "
            f"Id:{self.id}, Price: {self.price}, "
            f"{package.describe()}"
        )    

    @abstractmethod
    def type(self) -> str:
        pass
        
    @abstractmethod
    def foodPackage(self)->FoodPackage:
        pass  

class Hamburger(Product):

    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburguesa"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
class Soda(Product):
    
    def type(self):
        return "Soda"
    def foodPackage(self):
        return Bottle()

class Drink(Product):
    
    def type(self):
        return "Drink"

    def foodPackage(self):
        return "Bottle"

class HappyMeal(Product):
    
    def type(self):
        return "HappyMeal"

    def type(self):
        return Box()    
