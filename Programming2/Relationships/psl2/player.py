class Player:

    def __init__(self, name,sn,age,pt,country):

        self.name  = name
        self.shirtNum = sn
        self.age = age
        self.playerType = pt
        self.country  = country
    
    def display_player_properties(self):

        print(self.name,self.age,self.country,self.shirtNum,self.playerType)
    