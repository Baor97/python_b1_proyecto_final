from users.user import Cashier, Customer
from products.product import Product

class Order:
  def __init__(self, cashier:Cashier, customer:Customer):
    self.cashier = cashier
    self.customer = customer
    self.products = []

  def add(self, product : Product):
    self.products.append(product)

  def calculateTotal(self) -> float:
    return sum(p.price for p in self.products)
  
  def show(self):    
    print("Hello : "+self.customer.describe())
    print("Was attended by : "+self.cashier.describe())

    for i, product in enumerate(self.products, 1):
      print(f"Product {i}: {product.describe()}")

    print(f"Total price : {self.calculateTotal()}")
