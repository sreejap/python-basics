# Define a custom class
class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating
    
    # this is like println  in java
    def __repr__(self):
        return f"{self.name}: ${self.price}" 
