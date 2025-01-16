import datetime 
class Date:
    def date_in_future(self,integer_date):
        present_day = datetime.datetime.today()
        result = int(integer_date) if integer_date.isdecimal() else None
        if(result == None):    
            print(present_day)
        else:
            print((present_day + datetime.timedelta(days=result)).strftime('%d-%m-%Y %H:%M:%S'))
        return
class Main:
    print("Введите число дней будещего: ")
    date_future = input()
    date = Date()
    print("Результат работы программы")
    date.date_in_future(date_future)