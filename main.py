
import reciept
import device


kind = input("Выберете тип устройства (Ноутбук, Телефон, Телевизор): ")
brand = input("Введите брэнд устройства: ")
operation_system = input("Укажите операционную систему: ")
year_of_issue = input("Укажите год выпуска: ")
fullname = input("Введите ФИО клиента: ")
breakdowndescription = input("Введите описание поломки: ")


def Kind():
    types = ['Ноутбук', 'Телефон', 'Телевизор']

    if kind == types[0]:
        diag = input("Введите размер диагонали: ")
        return device.Laptop(brand, operation_system, year_of_issue, diag)

    if kind == types[1]:
        return device.Phone(brand, operation_system, year_of_issue)

    if kind == types[2]:
        diag = input("Введите размер диагонали: ")
        return device.TV(brand, operation_system, year_of_issue, diag)

    else:
        print("Выбрано неизвестное устройство.")


print("Квитанция №:", device.Device.number, "Что сдано в ремонт:", Kind(),
      reciept.Reciept(fullname, breakdowndescription), sep = '\n')





