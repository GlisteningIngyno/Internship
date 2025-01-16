class Numbers:
    def multiply_numbers(self,list_numbers):
        if(list_numbers != []):
            list_result = [pir for i in list_numbers for pir in i]
            end = 1
            flag = False
            for i in range(len(list_result)):
                result = int(list_result[i]) if list_result[i].isdecimal() else None
                if(result == None):
                    continue
                else:
                    end *= result
                    flag = True
        else:
            print("None")  

        if(flag):
            print(end)
        else:
            print("None")
       
  
        return
class Main:
    print("Добро пожаловать, введите цифры")
    list_numbers = input()
    print("Результат работы")
    numbers = Numbers()
    numbers.multiply_numbers(list_numbers)