from support_staff import SupportStaff
class Team:

    def __init__(self ,name ,city,owner) -> None:
        self.team_name:str  = name
        self.team_city:str  = city
        self.team_owner:str = owner
        self.team_players:list = []
        self.team_support_staff:list= []


    def add_player(self, player):
        self.team_players.append(player)

    def player_list(self):
         print(self.team_players)

    def create_spport_staff(self,name,age,des,sal):
        #composition  creating object inside obj
        self.team_support_staff.append(SupportStaff(name,age,des,sal))

    def support_staff_list(self):
        print(self.team_support_staff)
        
        

        