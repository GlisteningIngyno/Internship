class Game:
    def rps_game_winner(self,plaer1,RPS1,plaer2,RPS2):
        if(RPS1 == RPS2):
            print(plaer1 +" "+ RPS1)
        else:
            if(RPS1== "P" and RPS2=="R"):
                print(plaer1 +" "+ RPS1)
            elif(RPS1=="P" and RPS2=="S"):
                print(plaer2 +" "+ RPS2)
            if(RPS1== "R" and RPS2=="P"):
                print(plaer2 +" "+ RPS2)
            elif(RPS1=="R" and RPS2=="S"):
                print(plaer1 +" "+ RPS1)
            if(RPS1== "S" and RPS2=="R"):
                print(plaer2 +" "+ RPS2)
            elif(RPS1=="S" and RPS2=="P"):
                print(plaer1 +" "+ RPS1)
        return

    list_game = []
    def reWrite(self, string):
        self.list_game = string.split(",")
        return
    def rps_game(self):
        if(len(self.list_game)>=5 or len(self.list_game)<=3):
            print("WrongNumberOfPlayersError")
        else:
            if((self.list_game[1]!="R" and self.list_game[1]!="P"and self.list_game[1]!="S")or (self.list_game[3]!="R" and self.list_game[3]!="P"and self.list_game[3]!="S")):
                print("NoSuchStrategyError")
            else:
                self.rps_game_winner(self.list_game[0],self.list_game[1],self.list_game[2],self.list_game[3])

class Main:
    print("Добро пожаловать в игру") 
    print("Введите данные игроков,через запятую,без пробелов: ")
    game = Game()
    game.reWrite(input())
    game.rps_game()