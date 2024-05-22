
import string
import random

def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class Ticket:
    def __init__(self, user: str , complain:str) -> None:
        self.id  = generate_id()          # should be a random number
        self.customer = user
        self.issue  = complain
    
