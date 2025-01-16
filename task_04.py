class SortList:
    def sort_list(self,list_sort):
        list_result = list_sort.split()
        indexMax = None
        indexMin = None
        max = 0
        min = 99999999
        for i in range(len(list_result)):
            result = int(list_result[i]) if list_result[i].isdecimal() else None
            if(result > max):
                max = result
                indexMax = i
            if(result < min):
                min = result
                indexMin = i 
        if(list_result == []):
            return
        else:
            list_result[indexMax] = min
            list_result[indexMin] = max
            list_result.append(min)
        print(" ".join(map(str,list_result)))
        return

class Main:
    print("Введите список элементов: ")
    list_sort = input()
    print("Результат работы программы: ")
    sortList = SortList()
    sortList.sort_list(list_sort)