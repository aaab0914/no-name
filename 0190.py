class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            total = amount * self.price
            print(f"Sold {amount} {self.name}. Total:"
f"${total}")
        else:
            print(f"Not enough {self.name} in stock")
            
    def restock(self, amount):
        self.quantity += amount
        print(f"Restocked {amount} {self.name}. New quantity"
f":{self.quantity}")
    
    def display_info(self):
        print(f"Product: {self.name}, Price: ${self.price},"
f"Stock: {self.quantity}")
        
product1 = Product("Laptop", 999, 10)
product1.display_info()
product1.sell(3)
product1.restock(5)