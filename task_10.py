class Dictionary: 
    def corrector_string(self,list_symbol):
        list_finaly = []
        list_result = list_symbol.lower().split()
        for result in list_result:
            for peer in result.split(","):
                list_symbol_2 = [part for i in peer for part in i]
                for i in range(len(list_symbol_2)):
                    if(list_symbol_2[i] == "-"):#на место "-" можно поставить список с знаками препинания
                        list_symbol_2[i] = ""
                peer = ''.join(map(str,list_symbol_2))
                if(peer == ""): break
                list_finaly.append(peer)
        print(list_finaly)
        return list_finaly

    def count_words(self,list_symbol):
        list_word = self.corrector_string(list_symbol)
        new_dict = dict.fromkeys(list_word,0)
        for i in range(len(list_word)):
            if(list_word[i] in new_dict):
                new_dict[list_word[i]]+=1
        print(new_dict)
        

class Main:
    print("Добро пожаловать")
    list_symbol = input("Введите предложение: ")
    dictionary = Dictionary()
    dictionary.count_words(list_symbol)