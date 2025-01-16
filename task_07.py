class Anagrama:
    dictionary ={
    "cars":["cars","racs","scar"],
    "racs":["cars","racs","scar"],
    "scar":["cars","racs","scar"],
    "for":"four",
    "four":"for",
    "potatoes":"potatoes",
    "creams":["creams","scream"],
    "scream":["creams","scream"],
    }
        
    def combine_anagrams(self,words_array):
        list_term = words_array.split(",")
        for i in list_term:
            if(i in self.dictionary):
                print(self.dictionary.get(i))
            else:
                print("Такого слова в словаре нет")
        return
class Main:
    print("Добро пожаловать!")
    print("Введите список слов: ")
    list_elem = input()
    anagram = Anagrama()
    anagram.combine_anagrams(list_elem)
