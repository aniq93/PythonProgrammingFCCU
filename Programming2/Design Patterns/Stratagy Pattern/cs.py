from ticket import Ticket
import random

from abc import ABC , abstractmethod

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self,listOfTickets):
        pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, listOfTickets ):
        return listOfTickets.copy()
    
class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, listOfTickets):
        list_copy = listOfTickets.copy()
        list_copy.reverse()
        return list_copy
    
class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, listOfTickets):
        list_copy = listOfTickets.copy()
        random.shuffle(list_copy)
        return list_copy

class BlackHoleStrategy(TicketOrderingStrategy):
    def create_ordering(self, listOfTickets):
        return []


class CustomerSupport:

    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.tickets = []
        self.processing_strategy = processing_strategy
    
    def set_processing_strategy(self , processing_strategy):
        self.processing_strateg = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(Ticket(customer, issue))

    def process_tickets(self):
        # create the ordered list
        ticket_list = self.processing_strategy.create_ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: Ticket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")
