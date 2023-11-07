from product import Product
from store import Store

if __name__ == "__main__":
    my_store = Store("White Night")

    product_1 = Product("Bino", 19.99, "Board Game")
    product_2 = Product("Ramy", 9.99, "Cards Game")
    product_3 = Product("Dominoes", 14.99, "Scoring Game")

    my_store.add_product(product_1).add_product(product_2).add_product(product_3).sell_product(2).inflation(12).set_clearance(product_1.category, 25)
    
    for product in my_store.products:
        product.print_info()