from Trackable.trackable import Trackable
class Product(Trackable):
    def __init__(self, prod_id, name, price, stock_q):
        super().__init__(prod_id, name)
        self.price = price
        self.stock_q = stock_q
    def update_stock(self, quantity):
        self.stock_q -= quantity
    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock_q