class Product:
    def __init__(self, prod_id, name, price, stock_q):
        self.prod_id = prod_id
        self.name = name
        self.price = price
        self.stock_q = stock_q
    def update_stock(self, quantity):
        self.stock_q -= quantity