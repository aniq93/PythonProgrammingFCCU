'''

Encapulation : Wrapping of data and methods into a single unit with protection
Inheritance : Inheriting properties of parent class
Polymorphism : Many forms
Relationalship : Association, Aggregation, Composition and Inheritance



Abstraction : Hiding the implementation details and showing only the functionality

What is abstraction? 
Answer: Abstraction is a process of hiding the IMPLEMENTATION DETAIL
        and SHOWING only FUNCTIONALITY to the user.

        We have just the IDEA
        Not Conclusion


Absrtact Art 

Base Enemy:  Health, Damage, Movement, Attack  (Abstract)


Minnion(Base Enemy): Health(100), Damage(10), Movement(slow), Attack(2 moves) , multiply

Giant(Base Enemy): Health(500), Damage(50), Movement(medium), Attack(3 moves) , Grow

Boss(Base Enemy): Health(1000), Damage(100), Movement(fast), Attack(5 moves) , Power up eating minions


Abstract Class:
- Abstract class is a class that contains one or more abstract methods
  abstract method: method that is declared but not implemented



Social meadia:
      @abstractmethod
    - login credentials
      @abstractmethod
    - friends/followers
      @abstractmethod
    - chat

Facebook(Social media):
    - login credentials
    - friends/followers
    - chat
    
Instgram(Social media):
    - login credentials
    - friends/followers
    - chat

        
X(Social media):
    - login credentials
    - friends/followers
    - chat
    


Interface:
- Interface is a class that contains only abstract methods

Interface is like a strict contract



Abstract class vs Interface
- Abstract class can have abstract and non abstract methods
- Interface can have only abstract methods



'''

#from abc import ABC, abstractmethod     # abstract base class

# class Vehicle(ABC):
#     @abstractmethod
#     def movement(self):
#         pass
#     @abstractmethod
#     def ab2(self):
#         pass

#     def display(self):
#         print("This is vehicle")


# class Bicycle(Vehicle):
#     def movement(self):
#         print("Cycle is moving")

#     def ab2(self):
#         pass

#     def horn(self):
#         print("Honk Honk")


# cycle = Bicycle()
# cycle.display()
# cycle.movement()
# cycle.horn()



# def func(x:int , y:int)->int:
#         return x+y

# print(func("ok",5))


# class A(ABC):                         # INTERFACE
#     @abstractmethod
#     def go(self):
#         pass
     
#     def random(self):
#         pass

# # class B(A):
# #     # def go(self):
# #     #     print("I am B")

# #     def ok(self):
# #         print("I am ok ")

# # x = B()
# # x.ok()
# # # x.go()
# # # x.random()


from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self) -> None:
        self.a = "a"
        self.b = "b"
    @abstractmethod
    def movement(self):
        pass

class Lion(Animal):
    def movement(self):
        print("Walk on 4 legs")

class Parrot(Animal):
    def movement(self):
        print("Fly with 2 wings")


bird = Parrot()
print(bird.a)
bird.a  = "g"
print(bird.a)
lion = Lion()
print(lion.a)
