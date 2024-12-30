import uuid

from Sale.sale import Sale


class SalesTracker:
    def __init__(self):
        self.products = []
        self.customers = []
        self.sales = []

    def add_product(self, product):
        index = 0
        while index < len(self.products) and self.products[index].get_id() < product.get_id():
            index += 1
        self.products.insert(index, product)

    def regiseter_customer(self, customer):
        index = 0
        while index < len(self.customers) and self.customers[index].get_id() < customer.get_id():
            index += 1
        self.customers.insert(index, customer)

    def bin_search(self, arr, targ):
        l, r = 0, len(arr) - 1

        while l < r:
            m = (l + r) // 2
            if arr[m] < targ:
                l = m + 1
            elif arr[m] > targ:
                r = m - 1
            else:
                return m
        return -1

    def record_sale(self, c_id, p_id, q):
        customer = None
        product = None
        if (c := self.bin_search(self.customers, c_id)) < 0:
            raise Exception('Customer with corresponding ID is not registered')
        else:
            customer = self.customers[c]

        if (p := self.bin_search(self.products, p_id)) < 0:
            raise Exception('Product with corresponding ID is not registered')
        else:
            product = self.products[p]
            if product.get_stock() < q:
                raise ValueError('Insufficient stock available')
            product.update_stock(q)
        unique_id = self.generate_sale_id()
        sale = Sale(unique_id, customer, product, q)
        self.sales.append(sale)

    def generate_sale_id(self):
        return str(uuid.uuid4())


    def generate_report(self):
        revenue = 0
        for sale in self.sales:
            sale.calculate_total_price()
            revenue += sale.tot_prices
        print(revenue)