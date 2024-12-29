from collections import defaultdict


class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def get_contact(self):
        contact = defaultdict(str)
        contact['id'] = str(self.customer_id)
        contact['name'] = self.name
        contact['email'] = self.email
        contact['phone'] = self.phone
        return contact
