import datetime


class Employee:
    def __init__(self, fname, lname, add, phone, salaried, start, salary):
        self.first_name = str(fname)
        self.last_name = str(lname)
        self.address = str(add)
        self.phone_number = str(phone)
        self.salaried = bool(salaried)
        self.start_date = start
        self.salary = salary

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, add):
        self.address = add

    def set_phone_number(self, phone):
        self.phone_number = phone

    def set_salaried(self, salaried):
        self.salaried = salaried

    def set_start_date(self, start):
        self.start_date = start

    def set_salary(self, salary):
        self.salary = salary

    def display(self):
        message = str(self.first_name) + " " + str(self.last_name) + "\n" + str(self.address) + "\n"
        if self.salaried:
            message = message + "Salaried employee: $" + str(self.salary) + "/year\n"
        else:
            message = message + "Hourly employee: $" + str(self.salary) + "/hour\n"
        message = message + "Start date: " + self.start_date.strftime("%m") + '-' + self.start_date.strftime('%d') + \
                  '-' + self.start_date.strftime('%Y')
        return message


'''# Driver
dt = datetime.datetime(2019, 6, 28)
emp =  Employee('Sasha', 'Patel', '123 Main Street\nUrban, Iowa', '123-456-7890', True,  dt, 40000)
emp2 = Employee('Sasha', 'Patel', '123 Main Street\nUrban, Iowa', '123-456-7890', False, dt, 7.25)
print(emp.display())
print('--------------')
print(emp2.display())'''
