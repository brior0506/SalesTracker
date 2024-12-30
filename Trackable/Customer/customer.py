from collections import defaultdict

from Trackable.trackable import Trackable


class Customer(Trackable):
    def __init__(self, customer_id, name, email, phone):
        super().__init__(customer_id, name)
        self.email = email
        self.phone = phone

    def get_contact(self):
        contact = defaultdict(str)
        contact['id'] = str(self.customer_id)
        contact['name'] = self.name
        contact['email'] = self.email
        contact['phone'] = self.phone
        return contact


    def get_email(self):
        return self.email
    def get_phone(self):
        return self.phone

