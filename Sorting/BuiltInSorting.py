# Define a custom class
class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"{self.name}: ${self.price}"

products = [
    Product("Laptop", 999, 4.5),
    Product("Mouse", 25, 4.8),
    Product("Keyboard", 79, 4.2),
    Product("Monitor", 299, 4.6)
]

# Sort by price (ascending)
by_price = sorted(products, key=lambda p: p.price)
print(by_price)
# [Mouse: $25, Keyboard: $79, Monitor: $299, Laptop: $999]

# Sort by rating (descending)
by_rating = sorted(products, key=lambda p: p.rating,
                  reverse=True)
print(by_rating)
# [Mouse: $25, Monitor: $299, Laptop: $999, Keyboard: $79]

# Sort by name length
by_name_length = sorted(products, key=lambda p: len(p.name))
print(by_name_length)
# [Mouse: $25, Laptop: $999, Monitor: $299, Keyboard: $79]

# Sort by multiple criteria: price, then rating
by_price_then_rating = sorted(products,
    key=lambda p: (p.price, -p.rating)
)
