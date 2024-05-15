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
