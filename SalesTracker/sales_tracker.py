class SalesTracker:
    def __init__(self):
        self.products = []
        self.customers = []
        self.sales = []
    def add_product(self, product):
        self.products.append(product)
    def regiseter_customer(self, customer):
        self.customers.append(customer)

    def record_sale(self, c_id, p_id, q):
