<<<<<<< HEAD

class Device:
    type = ""
    operation_system = ""
    year_of_issue = ""




    def __init__ (self, type, name, operation_system, year_of_issue):
        self.type = type
        self.name = name
        self.operation_system = operation_system
        self.year_of_issue = year_of_issue



    def __str__(self):
        self.name = input("Укажите брэнд устройства: ")
        self.operation_system = input("Укажите операционную систему: ")
        self.year_of_issue = input("Укажите год выпуска: ")
        type = self.__class__.__name__
        return f"Наименование изделия: {type}\nБрэнд: {self.name} \n"\
               f"Операционная система: {self.operation_system}\nГод выпуска: {self.year_of_issue}"


class Laptop (Device):

    def __init__(self, name,  operation_system, year_of_issue, diag1):
        super(). __init__(type, name, operation_system, year_of_issue)
        self.diag1 = diag1

    def __str__(self):
        self.diag1 = input("Укажите длину диагонали: ")
        return f"{super().__str__()}\nДиагональ: {self.diag1}"



class Phone (Device):

    def __init__(self, name,  operation_system, year_of_issue):
        super(). __init__(type, name, operation_system, year_of_issue)

    def __str__(self):
        return f"{super().__str__()}"


class TV (Device):

    def __init__(self, name,  operation_system, year_of_issue, diag2):
        super(). __init__(type, name, operation_system, year_of_issue)
        self.diag2 = diag2


    def __str__(self):
        self.diag2 = input("Укажите длину диагонали: ")
        return f"{super().__str__()}\nДиагональ: {self.diag2}"










=======
print("Hello")
>>>>>>> origin/dev
