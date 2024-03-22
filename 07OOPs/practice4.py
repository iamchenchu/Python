class Inventory:
    shop_name = "Big Bazaar"
    location = "Hyderabad"
    stock = {}

    def __init__(self, item_name, item_price, item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def display(self):
        print(f"{self.item_name} is available at {Inventory.shop_name} for Rs.{self.item_price} per item")
    
    def add_stock(self):
        Inventory.stock[self.item_name] = self.item_quantity
        print(f"{self.item_quantity} {self.item_name} items are added to the stock")
    
    def sell(self, item_name, quantity):
        if item_name in Inventory.stock and Inventory.stock[item_name] >= quantity:
            Inventory.stock[item_name] -= quantity
            print(f"{quantity} {item_name} items are sold successfully, now the available quantity is {Inventory.stock[item_name]}")
        else:
            print(f"Sorry, the {item_name} items are not available in the stock")
            
    @staticmethod
    def display_stock():
        print(f"Available stock in {Inventory.shop_name} is {Inventory.stock}")


item1 = Inventory("Rice", 50, 100)
item2 = Inventory("Dal", 100, 50)
item3 = Inventory("Sugar", 40, 150)
item4 = Inventory("Oil", 200, 30)
item5 = Inventory("Wheat", 30, 200)

item1.display()
item2.display()
item3.display()
item4.display()
item5.display()

item1.add_stock()
item2.add_stock()
item3.add_stock()
item4.add_stock()
item5.add_stock()

Inventory.display_stock()


