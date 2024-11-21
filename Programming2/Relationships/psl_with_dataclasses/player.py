from dataclasses import dataclass

@dataclass
class Player:
#instance variables
    name:str
    age:int
    player_type:str
    player_sal:float
    player_country:str
    is_internation:bool
    runs:int
    wickets:int


