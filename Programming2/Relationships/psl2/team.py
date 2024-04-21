from support_staff import SupportStaff
class Team:

    def __init__(self, name, city,owner):
        self.name  = name
        self.city = city
        self.owner = owner
        self.titles = None
        self.player_pool = []
        self.supoort_staff_pool = []
    
    def add_player(self, player):
        
        self.player_pool.append(player)

    def display_team_properties(self):

        print(self.name, self.city,self.owner,self.titles,self.player_pool,self.supoort_staff_pool)
    
    def creat_support_staff(self,name,id,desg,exp):

         # this will create suporrt staff

        spStaff =  SupportStaff(name, id,desg,exp) #COMPOSITION

        self.supoort_staff_pool.append(spStaff)

        return spStaff