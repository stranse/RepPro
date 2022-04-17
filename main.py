
import reciept
import device

kind = input("Выберете тип устройства (Ноутбук, Телефон, Телевизор): ")
fullname = input("Введите ФИО клиента: ")
breakdowndescription = input("Введите описание поломки: ")


def Kind():
    types = ['Ноутбук', 'Телефон', 'Телевизор']

    if kind == types[0]:
        return str(device.Laptop('', '', '', '',''))

    if kind == types[1]:
        return str(device.Phone('', '', '',''))

    if kind == types[2]:
        return str(device.TV('', '', '', '', ''))

    else:
        print("Выбрано неизвестное устройство.")


print("Квитанция №:", device.Device.number, "Фамилия имя отчество клиента:", fullname, "Что сдано в ремонт:", Kind(),
       "Описание неисправности:", breakdowndescription, reciept.Reciept('', '', '', ), sep = '\n')





