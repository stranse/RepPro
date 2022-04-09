

import reciept
import utils



def Output():

    with open("output.txt", "a+") as f:
        print("Квитанция №: ", reciept.Number('').AddNum(), file=f)
        print("ФИО клиента: ", reciept.FullName('','',''), file=f)
        print(utils.Kind('',''), file=f)
        print(reciept.BreakdownDescription(''), file=f)
        print("Дата приемки в ремонт: ", reciept.GettingDate('').datetime(), file=f)
        print("Статус заказа: ", reciept.Status('',''), file=f)
        print("Дата выдачи заказа: ", reciept.FinishingDate('').findate(), file=f)
        print("---------------------------------", file=f)


    f.close()
=======
print("Hello")
>>>>>>> origin/dev
