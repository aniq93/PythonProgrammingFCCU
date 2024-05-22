'''
Customer Support (List of Tickets)

Ticket (ticket no, user, complain)


'''
from cs import CustomerSupport
from cs import *

strategy = RandomOrderingStrategy()

app = CustomerSupport(strategy)

app.create_ticket('anique','please study hard guys')
app.create_ticket('Akheem','dont mess up')
app.create_ticket('Kholi', 'Tere se nai hta chase')

app.process_tickets()

app.set_processing_strategy(FIFOOrderingStrategy())
app.process_tickets()
