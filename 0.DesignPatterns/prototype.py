#single object as a prototype and keep reusing one element
#in below example reusing address just using deepcopy we can
#implement prototype method.

import copy

class Address:
    def __init__(self,city, country):
        self.city=city
        self.country=country

    def __str__(self):
        return "{}, {}".format(self.city, self.country)

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return "{} lives in {}".format(self.name, self.address)


class EmployeeFactory:
    #main office at bangalore
    main_office_employee = Employee('', Address('Banglore','India'))
    aux_office_employee = Employee('', Address('Hyderabad','India'))

    @staticmethod
    def _new_employee(proto,name):
        result = copy.deepcopy(proto)
        result.name = name

    @staticmethod
    def new_main_office_employee(name):
        return EmployeeFactory._new_employee(
            EmployeeFactory.main_office_employee,
            name
        )

    @staticmethod
    def aux_main_office_employee(name):
        return EmployeeFactory._new_employee(
            EmployeeFactory.aux_office_employee,
            name
        )

# rahul = Person('Rahul', Address('Banglore','India'))
# import copy
#
# ragini = copy.deepcopy(rahul)
# ragini.name='Ragini'
#
# print(rahul,ragini)

