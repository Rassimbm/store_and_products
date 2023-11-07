# Start by creating a Store class that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.
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
# Next, create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.
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

if __name__ == "__main__":
    my_store = Store("White Night")

    product_1 = Product("Bino", 19.99, "Board Game")
    product_2 = Product("Ramy", 9.99, "Cards Game")
    product_3 = Product("Dominoes", 14.99, "Scoring Game")

    my_store.add_product(product_1).add_product(product_2).add_product(product_3).sell_product(2).inflation(12).set_clearance(product_1.category, 25)
    
    for product in my_store.products:
        product.print_info()