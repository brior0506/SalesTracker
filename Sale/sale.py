class Sale:
    def __init__(self, sale_id, customer, product, quantity):
        self.sale_id = sale_id
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.tot_prices = 0
    def calculate_total_price(self):
        self.tot_prices = self.product.get_price() * self.quantity
