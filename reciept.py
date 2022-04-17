
import random
import datetime

class Reciept:

    position = ['Готово', 'В работе', 'Выдано клиенту']

    def __init__(self, gettingdate, finishingdate, status):
        self.gettingdate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        self.finishingdate = (datetime.datetime.now() +
                              datetime.timedelta(days = random.randint(1, 5))).strftime("%d-%m-%Y %H:%M")
        self.status = random.choice(Reciept.position)

    def __str__(self):
        return f'Дата приемки изделия: {self.gettingdate}\n' \
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



