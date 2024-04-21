from team import Team

from player import Player


lahore  = Team("Lahore Qalanders", "Lahore" , "Rana Fawad")

lahore.display_team_properties()
x = lahore.creat_support_staff("Aqib Javed" , 1 , "Head Coach",20)

x.display_support_staff_properties()

lahore.display_team_properties()


shaheen  = Player("Shaheen Afridi", 10, 23 , "Bowler" , "Pakistan")

lahore.add_player(shaheen)
lahore.display_team_properties()

y = lahore.player_pool[0]
y.display_player_properties()

