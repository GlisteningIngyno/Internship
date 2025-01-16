class Palindrome:
    lst_new_symbol = []
    def convert_string(self,string):
        lst_symbol = [",",".","-","!","?","'",]
        j = 0
        lst = [part for i in string.lower().split() for part in i] 
        for i in range(len(lst)):
            while(True):
                if(lst[i] != lst_symbol[j]):
                    j+=1
                    if(j==len(lst_symbol)):
                        self.lst_new_symbol.append(lst[i])
                        j = 0
                        break
                    continue
                else:
                    j = 0
                    break  
         
    def is_palindrome(self, string):
        self.convert_string(string)
        temp = ""
        max_index = len(self.lst_new_symbol)-1
        for i in range(len(self.lst_new_symbol)):
            if(self.lst_new_symbol[i]==self.lst_new_symbol[max_index]):
                max_index-=1
                if(max_index <=0): return "True"
                continue
            else:
                return "False"
        return None
class Main:
    plnd = Palindrome() 
    input_str = input("Введите строку: ")
    print(plnd.is_palindrome(input_str))
       