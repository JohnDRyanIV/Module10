class Customer:
    def __init__(self, id, lname, fname, phone, add):
        try:
            if not isinstance(id, int):
                raise AttributeError
            else:
                self.customer_id = int(id)
        except AttributeError:
            self.customer_id = "AttributeError: 'Customer' object has no attribute 'cid'"

        self.last_name = str(lname)
        self.first_name = str(fname)
        self.phone_number = str(phone)
        self.address = str(add)

    def __str__(self):
        return 'Customer with id ' + str(self.customer_id) + ', last name ' + str(self.last_name) + ', first name ' \
               + str(self.first_name) + ', phone number ' + str(self.phone_number) + ', address ' + str(self.address)

    def __repr__(self):
        return 'Customer(id={},last_name={},first_name={},phone_number={},address={}' \
                .format(self.customer_id, self.last_name, self.first_name, self.phone_number, self.address)

    def display(self):
        message = str(self.last_name) + ', ' + str(self.first_name) + '\nID: ' + str(self.customer_id) + "\n"\
                      + str(self.phone_number) + '\n' + str(self.address)
        return message


# Driver
customer1 = Customer(1029384, 'Pratchet', 'Harold', '515-555-1111', '123 Alphabet Road, Hell Town, Ohio')
customer2 = Customer('1029384f', 'Pratchet', 'Harold', '515-555-1111', '123 Alphabet Road, Hell Town, Ohio')
print(str(customer1))
print(repr(customer1))
print("----------")
print(str(customer2))
print(repr(customer2))
print("----------")
print(customer1.display())
print("----------")
print(customer2.display())
