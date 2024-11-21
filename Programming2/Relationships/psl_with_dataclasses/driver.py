'''
player                  team                         support_staff

name                    team_name:str                support_name:str
age                     team_city:str                support_age:int
player_type             team_owner:str               support_designation:str
player_sal              team_players:[]              support_sal:int
player_country          support_staff_list:[]                          
runs 
wicktets                add_player()                 support_details
                        remove_player()
stats                   add_suppport_staff()
                        remove_support_staff
                        create_training_session()
                        start_training_session()
                        end_training_session()


    
                        

player pool(players, players, players, players)


player -->aggregation--> team 

support_staff --> composition --> team

'''

from player import Player
from team import Team

shaheen =Player("Shaheen Shah Afridi" , 25 , 
                "Bowler" , 25000 , "Pakistan",
                False , 0, 0)
babar =Player("Babar Azam" , 26 , 
                "Batsman" , 30000 , "Pakistan",
                False , 0, 0)

lahore = Team("Lahore Qalander" , "Lahore" , "Rana")


#Aggregation  passing object to the independent class as prameter
lahore.add_player(shaheen)
lahore.add_player(babar)


lahore.player_list()

lahore.create_spport_staff("Aqib Javed" , 50 , "Head Coach" , 10000)

lahore.support_staff_list()

