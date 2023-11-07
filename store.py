# Create a Store class that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.
class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

# Let's also give some methods to our Store class:

# add_product(self, new_product) - takes a product and adds it to the store
    def add_product(self, new_product):
        if new_product not in self.products:
            self.products.append(new_product)
        else:
            print(f"The store: {self.name} already has a product named {new_product}")
        return self
# sell_product(self, id) - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
    def sell_product(self, id):
        if id >= 0 or id <= len(self.products):
            sold_product = self.products.pop(id)
            sold_product.print_info()
        else:
            print(f"Invalid product ID!!!")
        return self
# inflation(self, percent_increase) - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self
# set_clearance(self, category, percent_discount) - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self



