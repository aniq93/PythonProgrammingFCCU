'''
-helps yoy write more data oriented classes
data oriented class - Point Vector 
behavior oriented class - Payment service Button 

Helps - represnet as string, add easy implementation to initiaize , compare object
'''
# import random 
# import string
from dataclasses import dataclass , field

# def generate_id() -> str:
#     return "".join(random.choices(string.ascii_letters,k=5))

@dataclass
class Person:
    name:str
    address:str
     
    # email_list : list[str] = field(default_factory=list)
    # id:str = field(default_factory=generate_id)
    # search_string: str = field(init=False , repr=True)

    def __post__init__(self) -> None:
        pass
   

person = Person('1123','Lahore')



print(person.address)

 