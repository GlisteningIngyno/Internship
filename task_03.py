class ArbitraryNature:
    def max_odd(self, array):
        max = 0
        list_symbol = array.split()
        for i in range(len(list_symbol)):
            result = float(list_symbol[i]) if self.isfloat(list_symbol[i]) else None
            if(result == None):
                continue
            else:
                if(result>max and result%2!=0):
                    max = result
        if(max == 0):
            print("None")
        else:
            print(max)
        return

    def isfloat(self,string):
        try:
            result = float(string)
            return result
        except ValueError:
            return None
    
class Main:
    print("Введите список произвольной природы ")
    list_symbol = input()
    print("Результат работы программы: ")
    arbitraryNature = ArbitraryNature()
    arbitraryNature.max_odd(list_symbol)
