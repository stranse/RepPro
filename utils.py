import device

class Kind:
    
    def __init__(self, kind, types):
        self.kind = kind
        self.types = types
        
    def __str__(self):
        self.kind = input("Введите тип устройства: ")
        self.types = ['Ноутбук','Телефон','Телевизор']

        if self.kind == self.types[0]:
            return str(device.Laptop('','','',''))

        if self.kind == self.types[1]:
            return str(device.Phone('','',''))

        if self.kind == self.types[2]:
            return str(device.TV('','','',''))

        else:
            return f'Выбрано неизвестное устройство'



# def create_counter():
#     i = 0
#
#     def func():
#         nonlocal i
#         i += 1
#         return i
#     return func
# class IncrementCounter:
#
#     def __init__(self):
#         self._value = 0
#
#     def new_value(self):
#         self._value += 1
#         return self._value


            