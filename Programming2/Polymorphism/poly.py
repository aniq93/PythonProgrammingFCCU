# Polymorphism #

 #Poly - > Many  morph -> shapes # 

## Duck typing, Operator Overloading, Method Overloading, Method Overriding ###


 # Duck Typing #      ### One METHOD name differnet shapes 
                         ### Dont care about the class type. But method name should be same

                         ### Dynamic Typing a = int , a = str
    
                         ### int a  = 5  ,   a = 'aniq'
# class Bird:
#     def fly(self):
#         print("weeee I can fly Bird")
# class Aeroplane:
#     def fly(self):
#         print("Weee I can fly Aeroplane")
# class Fish:
#     def swim(self):
#         print ("Wee I can swim")

# for i in Bird(),Aeroplane():
#     i.fly()
   
# x = Bird()
# x= Aeroplane()
# x.fly()


## OPERATOR OVERLOADING ##
#Same + __add__
# #Different  sum , concatnate 
# x = 5 + 5
# print(x)

# y = 5 
# y  = y.__add__(5)
# print(x)
# print(y)


# x = "Computer" + "Science"

# y = "Computer"
# y  = y.__add__("Science")
# print(x)
# print(y)
# print(y)
# y = int(5)

# x = "This is a string"
# y = str("this iss string")

# obj = Fish()
# print(type(obj))


# x = 5
# x = int(5)

# print(type(x))


# ### Operator Overloading   ### + - / *  Magic Methods

# x =  5 + 6 

# x = int(5)

# x = x.__add__(6)

# print(x)

# a = 6 
# b  = "age"
# c = 7
# d = "babar"
# print(a + c)
# print(b + c)

# print(int.__add__(a,b))
# print(str.__add__(b,d))


class Employe():
    def __init__(self,sal):
        self.salary = sal

    def __add__ (self,obj):
        total_sal = self.salary + obj
        # print(self.salary,obj.salary)
        return total_sal

    def __mul__ (self,obj):
        sal = self.salary * obj.salary
        return sal
    def __mod__ (self,obj):
        print("Babar Azam Zindabad")
        return self
    

asim = Employe(30000)
print(asim.salary)

azhar  = Employe(40000)
print(azhar.salary)

total_sal = asim + 40000
# total_sal1 = asim.__add__(azhar)

print(total_sal)


x = asim % azhar
print(x.salary)

# #print(azhar.salary)

# # x = asim % azhar

# x  = asim.__add__(azhar)

# y = asim * azhar

# print(y)



# tiktok = asim + azhar

# print(Employe.__add__(asim,azhar))

# print(tiktok)

# ticktok = asim * azhar

# print(ticktok.salary)


# Method Overloading ###

# class A:                    # Same name differnet parameters  
#                               # Within same class
#     def admin(self,a,b):
#         return a+b
#     def admin(self,a,b,c):
#         return a+b+c
#     def admin(self,a):
#         return a

# a = A()
# a.admin(4,3,4)


# class Calculator:
    # def sum(self,a=None,b=None,c=None):
    #     if a !=None and b  != None and c != None:
    #          s = a + b + c
    #          print("case 1")
    #          return s
    #     elif a!=None and b!=None and c==None:
    #         s = a + b
    #         print("case 2")
    #         return s
    #     elif a!=None and b==None and c==None:
    #         print("case 3")
    #         return a
        
    #     return s

#     def sum(self,*args):
#         if len(args)< 4:
#             result = 0
#             for i in args:
#                 result = result + i
#             return result
#         else:
#             print('To many argument')
        
            

# obj  = Calculator()
# print(obj.sum(2,3))


# class Calculator: 
#     def add(a:int ,b: int, c = None , d = None) -> int:

#         if c  == None and d == None:
#             return a+b 
        
#         elif d == None:
#             return a+b+c
        
#         else:
#             return a+b+c+d

# calc = Calculator

# print(calc.add(1,2,2,4))

       
        # if c == None and d == None:
        #     return a+b 
        # elif d == None:
        #     if type(c) == int:
        #         return a + b + c
        # else:
        #     if type(d) == int and type(c) == int:
        #         return a+b+c+d
        #     else:
        #         print("Type mismatched")






# ##Method Over Riding ##               # differnet class(Parent Child) , same method name , differnet implenetation
# class Bank():
#     def get_rate_of_interest(self):
#         return 2

# class HBL(Bank):
#     def get_rate_of_interest(self):
#         return 8
#     pass
    

# class HBLModelTown(HBL):
#     def get_rate_of_interest(self):
#         return 10
#     pass

# bank  = HBL()
# print(bank.get_rate_of_interest())

    
# bank1 = HBLModelTown()

# print(bank1.get_rate_of_interest())

# print("here")

# print(bank1.get_rate_of_interest())


# class Bank():
#     def get_interest_rate(self):
#         return 0.5

# class HBL(Bank):
#     pass
#     # def get_interest_rate(self):
#     #     return 1

# class HBLModelTown(HBL):
#     pass
#     # def get_interest_rate(self):
#     #     return 4


# bank  = HBLModelTown()
# print(bank.get_rate_of_interest())

# x = int(5)




# def fun(*args):
#     sum = 0
#     print(args)
#     for i in args:
#         sum = sum + i
#     print(sum)
# fun(1,2,4,5)