import device
import random
import datetime

class Reciept:

    number = 1
    position = ['Готово', 'В работе', 'Выдано клиенту']
    kind = input("Выберете тип устройства (Ноутбук, Телефон, Телевизор): ")

    def __init__(self, number, fullname, breakdowndescription, gettingdate, finishingdate, status):
        self.number = Reciept.number
        Reciept.number += 1
        self.fullname = input("Введите ФИО клиента: ")
        self.breakdowndescription = input("Введите описание поломки: ")
        self.gettingdate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        self.finishingdate = (datetime.datetime.now() +
                              datetime.timedelta(days = random.randint(1, 5))).strftime("%d-%m-%Y %H:%M")
        self.status = random.choice(Reciept.position)

    def Kind (self):
        types = ['Ноутбук', 'Телефон', 'Телевизор']

        if self.kind == types[0]:
            return str(device.Laptop('', '', '', ''))

        if self.kind == types[1]:
            return str(device.Phone('', '', ''))

        if self.kind == types[2]:
            return str(device.TV('', '', '', ''))

        else:
            print ("Выбрано неизвестное устройство, вам следует выбрать из указанного списка.")
            #print (Reciept.Kind (self))
            return (Reciept('','','','','',''))

    def __str__(self):
        return f'Квитанция №: {self.number}\n' \
               f'Фамилия Имя Отчество клиента: {self.fullname}\n'\
               f'Что сдано в ремонт: {Reciept.Kind(self)}\n' \
               f'Описание неисправности: {self.breakdowndescription}\n' \
               f'Дата приемки изделия: {self.gettingdate}\n' \
               f'Статус изделия: {self.status}\n' \
               f'Планируемая дата выдачи заказа: {self.finishingdate}'












# class FullName:
#
#     def __init__(self, surname, name, patronymic):
#         self.surname = surname
#         self.name = name
#         self.patronymic = patronymic
#
#         self.surname = input("Введите фамилию: ")
#         self.name = input("Введите имя: ")
#         self.patronymic = input("Введите отчество: ")
#
#     def __str__(self):
#         return f"ФИО: {self.surname} {self.name} {self.patronymic}"
#
#
# class GettingDate:
#
#     def __init__(self, now):
#         self.now = now
#
#     def datetime (self):
#         now = datetime.datetime.now()
#         #print("Дата и время приема изделия в ремонт:")
#         #print(now.strftime("%d-%m-%Y %H:%M"))
#         return now.strftime("%d-%m-%Y %H:%M")
#
#
#
# class Number:
#
#
#     def __init__(self, number):
#         self.number = number
#
#     def AddNum (self):
#         self.number = random.randint(1, 100)
#         #print("Квитанция: ", f"{self.number}")
#         return f"{self.number}"
#
#
# class FinishingDate(GettingDate):
#
#     def __init__(self, date):
#         super().__init__(date)
#
#     def findate(self):
#         now = datetime.datetime.now()
#         t = datetime.timedelta(days = 3)
#         Fin_day = now + t
#         Fin = Fin_day.strftime("%d-%m-%Y %H:%M")
#         #print("Дата завершения ремонта: ", Fin)
#         return Fin
#
#
# class BreakdownDescription:
#
#     def __init__(self, break_description):
#         self.break_description = break_description
#
#         self.break_description = input("Описание поломки: ")
#
#     def __str__(self):
#         return f"Описание неисправности: {self.break_description}"
#

# def status ():
#     position = ['Готово', 'В работе', 'Выдано клиенту']
#     return f'Статус устройства: {random.choice(position)}'



