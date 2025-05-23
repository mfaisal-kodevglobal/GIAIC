class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute convention
    
    @property
    def price(self):
        """Getter for price"""
        print("Getting price...")
        return self._price
    
    @price.setter
    def price(self, new_price):
        """Setter for price with validation"""
        print("Setting new price...")
        self._price = new_price
    
    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price

product = Product("Laptop", 999.99)

# Get price (uses @property)
print(f"Original price: {product.price}")

# Set price (uses @price.setter)
product.price = 899.99
print(f"Discounted price: {product.price}")

# Delete price (uses @price.deleter)
del product.price
