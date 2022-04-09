

class Device:
    type = ""
    operation_system = ""
    year_of_issue = ""

    def __init__ (self, type, brand, operation_system, year_of_issue):

        self.type = type
        self.brand = input("Введите брэнд устройства: ")
        self.operation_system = input("Укажите операционную систему: ")
        self.year_of_issue = input("Укажите год выпуска: ")


    def __str__(self):
        type = self.__class__.__name__
        return f"{type}\n" \
               f"Брэнд: {self.brand}\n"\
               f"Операционная система: {self.operation_system}\n" \
               f"Год выпуска: {self.year_of_issue}"

class Laptop (Device):

    def __init__(self, brand,  operation_system, year_of_issue, diag):
        super(). __init__(type, brand, operation_system, year_of_issue)
        self.diag = diag
        # self.diag = self.datadev[3]
        self.diag = input("Укажите длину диагонали: ")

    def __str__(self):
        return f"{super().__str__()}\nДиагональ: {self.diag}"

class Phone (Device):

    def __init__(self, brand,  operation_system, year_of_issue):
        super(). __init__(type, brand, operation_system, year_of_issue)

    def __str__(self):
        return f"{super().__str__()}"

class TV (Device):

    def __init__(self, brand,  operation_system, year_of_issue, diag):
        super(). __init__(type, brand, operation_system, year_of_issue)
        self.diag = diag
        self.diag = input("Укажите длину диагонали: ")

    def __str__(self):
        return f"{super().__str__()}\nДиагональ: {self.diag}"










