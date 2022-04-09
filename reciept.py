
import datetime
import random
import device



class FullName:

    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self):
        self.surname = input("Введите фамилию: ")
        self.name = input("Введите имя: ")
        self.patronymic = input("Введите отчество: ")
        return f"ФИО: {self.surname} {self.name} {self.patronymic}"


class GettingDate:

    def __init__(self, now):
        self.now = now

    def datetime (self):
        now = datetime.datetime.now()
        print("Дата и время приема изделия в ремонт:")
        print(now.strftime("%d-%m-%Y %H:%M"))
        return now.strftime("%d-%m-%Y %H:%M")



class Number:


    def __init__(self, number):
        self.number = number

    def AddNum (self):
        self.number = random.randint(1, 100)
        print("Квитанция: ", f"{self.number}")
        return f"{self.number}"


class FinishingDate(GettingDate):

    def __init__(self, date):
        super().__init__(date)

    def findate(self):
        now = datetime.datetime.now()
        t = datetime.timedelta(days = 3)
        Fin_day = now + t
        Fin = Fin_day.strftime("%d-%m-%Y %H:%M")
        print("Дата завершения ремонта: ", Fin)
        return Fin


class BreakdownDescription:

    def __init__(self, break_description):
        self.break_description = break_description

    def __str__(self):
        self.break_description = input("Описание поломки: ")
        return f"Описание неисправности: {self.break_description}"


class Status:

    def __init__(self, inwork, done):
        self.inwork = inwork
        self.done = done

    def __str__(self):
        self.inwork = input("Введите статус устройства: ")
        self.done = ['Готово', 'В работе', 'Выдано клиенту']

        if self.inwork == self.done[0]:
            return str(self.done[0])

        if self.inwork == self.done[1]:
            return str(self.done[1])

        if self.inwork == self.done[2]:
            return str(self.done[2])

        else:
            return f'Статус неизвестен'




















=======
print("Hello")
>>>>>>> origin/dev
