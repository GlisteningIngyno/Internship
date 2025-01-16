class WorkListRange:
    def coincidence(self, lst, rangeA,rangeB):
        list_symbol = lst.split() 
        list_result = []
        for i in range(len(list_symbol)):
            result = int(list_symbol[i]) if list_symbol[i].isdecimal() else None
            if(result == None):
                continue
            elif(result > rangeA and result <rangeB):
                list_result.append(result)
                
        print(" ".join(map(str,list_result)))
        return

class Main:
    print("Введите список элементов: ")
    list_symbol = input()
    print("Введите начальный диапозон: ")
    rangeA = int(input())
    print("Введите конечный диапозон: ")
    rangeB = int(input())
    print("Результат работы программы: ")
    workListRange = WorkListRange()
    workListRange.coincidence(list_symbol,rangeA,rangeB)