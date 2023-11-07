#   Create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

# Let's give some methods to our Product class:

# update_price(self, percent_change, is_increased) - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change) / 100
        else:
            self.price -= (self.price * percent_change) / 100
        return self
# print_info(self) - print the name of the product, its category, and its price.
    def print_info(self):
        print(f"Name: {self.name}\nPrice: ${self.price:.2f}\nCategory: {self.category}\n")
        return self 