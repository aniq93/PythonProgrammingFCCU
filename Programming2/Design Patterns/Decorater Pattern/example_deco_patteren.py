from abc import ABC, abstractmethod
from typing import Any

"""
1. Create basic concrete class
2. Implement using a Interface
             
            Notification Interface

        Notification    Decorater Base

                Fb Decoter SMS decorter Email

3. create object of concret class
4. feed it to the decorater class
5. Keep doing it until you have your requierd decorated output


"""



#interface
class NotifierInterface(ABC):
    """Basic notification sending."""
    @abstractmethod
    def send_data(message:str):
         """Prepare to send data"""

#concret class
class Notifier(NotifierInterface):
     def send_data(self,message: str):
          print(f"Message: {message} ")

          

class NotifierBaseDecorater(NotifierInterface):
     def __init__(self,notifier):
          print(f"In NBD __init__")
          self.notifier = notifier

     def send_data(self,message: str):
         print(f"In NBD send_data")
         return self.notifier.send_data(message)
          
class FacebookDecorater(NotifierBaseDecorater): 
     def send_data(self,message):
          print(f"Sending notification to Facebook :{message}")  
          return self.notifier.send_data(message)

class SMSDecorater(NotifierBaseDecorater):
    def send_data(self,message):
        print(f"Sending notification to SMS {message}")  
        return self.notifier.send_data(message) 

class EmailDecorater(NotifierBaseDecorater):
    def send_data(self,message):
        print(f"Sending notification to Email {message}")  
        return self.notifier.send_data(message)        



message = "Dr Mubashar has liked you post"

notification  = Notifier()
notification = FacebookDecorater(notification) #init
notification = SMSDecorater(notification)
notification = EmailDecorater(notification)

notification.send_data(message)

