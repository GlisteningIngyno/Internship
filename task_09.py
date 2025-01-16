class Dictionary:
    def connect_dicts(self,dict1,dict2):
        list_value1 = []
        list_value2 = []

        list_value1 = dict1.values()
        sum_value1 = sum(list_value1)

        list_value2 = dict1.values()
        sum_value2 = sum(list_value2)
           
        if sum_value1 > sum_value2:
            priority_dict = dict1
            secondary_dict = dict2
        else:
            priority_dict = dict2
            secondary_dict = dict1
        
        result_dict = {k: v for k, v in priority_dict.items() if v>=10}
        result_dict.update({k: v for k, v in secondary_dict.items() if v >= 10})
        get_dict = dict(sorted(result_dict.items(),key=lambda item: item[1]))
        print(get_dict)
        return

        

class Main:
    print("Добро пожаловать")
    dictionary = Dictionary()
    dictionary.connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })
    dictionary.connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) 
    dictionary.connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) 
