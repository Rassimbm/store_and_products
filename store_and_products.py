# Start by creating a Store class that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.
class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

# Next, create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
