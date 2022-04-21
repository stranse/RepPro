

class Device:
    type = ""
    operation_system = ""
    year_of_issue = ""
    number = 1

    def __init__ (self, brand, operation_system, year_of_issue):
        self.number = Device.number
        Device.number += 1
        self.brand = brand
        self.operation_system = operation_system
        self.year_of_issue = year_of_issue

    def __str__(self):
        type = self.__class__.__name__
        return f"{type}\n" \
               f"Брэнд: {self.brand}\n"\
               f"Операционная система: {self.operation_system}\n" \
               f"Год выпуска: {self.year_of_issue}"

class Laptop (Device):

    def __init__(self, brand,  operation_system, year_of_issue, diag):
        super(). __init__(brand, operation_system, year_of_issue)
        self.diag = diag

    def __str__(self):
        return f"{super().__str__()}\nДиагональ: {self.diag}"

class Phone (Device):

    def __init__(self, brand,  operation_system, year_of_issue):
        super(). __init__(brand, operation_system, year_of_issue)

    def __str__(self):
        return f"{super().__str__()}"

class TV (Device):

    def __init__(self, brand,  operation_system, year_of_issue, diag):
        super(). __init__(brand, operation_system, year_of_issue)
        self.diag = diag

    def __str__(self):
        return f"{super().__str__()}\nДиагональ: {self.diag}"










