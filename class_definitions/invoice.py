TAX = .06


class Invoice:
    def __init__(self, in_id, cus_id, lname, fname, phone, add, items=dict()):
        self.invoice_id = in_id
        self.customer_id = cus_id
        self.last_name = lname
        self.first_name = fname
        self.phone_number = phone
        self.address = add
        self.items_with_price = items

    def __str__(self):
        return 'Invoice with invoice id ' + str(self.invoice_id) + ', customer id ' + str(self.customer_id) + \
               ', last name ' + str(self.last_name) + ', first name ' + str(self.first_name) + ', phone number ' + \
               str(self.phone_number) + ', address ' + str(self.address) + ', items with price ' + \
               str(self.items_with_price)

    def __repr__(self):
        return "Invoice(invoice_id={},customer_id={},last_name={},first_name={},phone_number={},address={}," \
               "items_with_price={}" \
            .format(self.invoice_id, self.customer_id, self.last_name, self.first_name, self.phone_number,
                    self.address, self.items_with_price)

    def add_item(self, item):
        self.items_with_price.update(item)

    def create_invoice(self):
        total = 0
        list_a = list(self.items_with_price.keys())
        list_b = list(self.items_with_price.values())
        for index in range(len(list_a)):
            print(str(list_a[index]) + ".....$" + str(list_b[index]))
            total = total + list_b[index]
        print("Tax.........$" + format(round((total * TAX), 2), '.2f'))
        total = total + (total * TAX)
        print("Total.......$" + format(round(total, 2), '.2f'))


# Driver
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
print(str(invoice))
invoice.create_invoice()
