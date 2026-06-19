from abc import ABC, abstractmethod
from users.user import Cashier, Customer
from products.product import Hamburger, Soda, Drink, HappyMeal

class Converter(ABC):

  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):

  def convert(self, df, *args):
    return [
      Cashier(row["dni"], row["name"], row["age"], row["timetable"], row["salary"])
      for _, row in df.iterrows()
    ]

      
class CustomerConverter(Converter):
  
  def convert(self, df, *args):
    return [
      Customer(row["dni"], row["name"], row["age"], row["email"], row["postal_code"])
      for _, row in df.iterrows()
    ]

class ProductConverter(Converter):
  
  def convert(self, df, *args):
    products = []

    for _, row in df.iterrows():
      if row["type"] == "Hamburger":
        products.append(Hamburger(row["id"], row["name"], row["price"]))
        elif row["type"] == "Soda":
          products.append(Soda(row["id"], row["name"], row["price"]))
        elif row["type"] == "Drink":
          products.append(Drink(row["id"], row["name"], row["price"]))
        elif row["type"] == "HappyMeal":
          products.append(HappyMeal(row["id"],row["name"], row["price"]))
    
    return products
