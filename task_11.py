class Dessrt:
    def __init__(self,name ="",calories = 0):
        self._name = name
        self._calories = calories
        return

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self):
        self._name = new_name

    @property
    def calories(self):
        return self._calories
    @calories.setter
    def calories(self):
        self._calories = new_calories

    def is_healthy(self, calories):
        if(calories < 200): return True
        return False

    def is_delicious(self, name):
        if(name != " "): return True
        return False
class Main:
    print("Добро пожаловать")

    dessrt = Dessrt(input(),int(input()))
    print("Результат ввода: ")
    print(dessrt.name)
    print(dessrt.calories)
    dessrt.is_healthy(dessrt.calories)
    dessrt.is_delicious(dessrt.name)