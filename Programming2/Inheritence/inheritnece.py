# class Parent():
#     def __init__(self,a,b):
#         self.a = a      # parent attributes
#         self.__b = b
#                            # Parent ---> Child 
#     def concat(self):     #parent mthod
#         return self.a + self.b

# class Child(Parent):           # declaration     
#     def __init__(self,a,b,c):
#         # Parent.__init__(self,a,b)  # Invoke (Object creation)
#         super().__init__(a,b)
#         self.c = c


# child  = Child("This", "is" , "Ok")
# print(child.a)

# parent  = Parent()
# print(parent.a)
# print(parent.b)
# print(parent.concat())

# child = Child()

# print(child.c)
# print(child.b)
# print(child.concat())



# # print(child.concat())


# # SINGLE LEVEL INHERITENCE

# class Employee():
#     def __init__(self,name,id):
#         self.name  = name
#         self.id = id 


# class Teacher(Employee):
#     def __init__(self,name,id,dpt_name,dpt_id):
#         Employee.__init__(self,name,id)
#         self.deptId = dpt_id
#         self.deptName = dpt_name 


# class Admin(Employee):
#     def __init__(self,name,id, dpt_name, dpt_id):
#         Employee.__init__(self,name,id)
#         self.deptId = dpt_name
#         self.deptName  = dpt_id


# aniq = Teacher("Anique",1,"CS",51)

# gohar = Admin("Gohar",100,"Admisson",20)

# print(aniq.deptName,aniq.name)
# print(gohar.id)

# admin_list =[]
# for i in range(0,10):
#     # get value from user
#     admin_list.append(Admin())
# listitem = [1,2,3,4]

# print(listitem[1].)


# class Parent():
#     def __init__(self):
#         self.a =  "a"
#         self.b  = "b"

#     def concat(self):
#         return self.a + self.b

# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)
#         self.c = "c"
# # parent = Parent()

# # child  = Child()

# # print(child.a)
# # print(child.b)
# # print(child.c)

# # SINGLE LEVEL INHERITENCE

## PARENT ---- >> CHILD

class Researcher:
    def __init__(self,active,num,hip):
        self.activeResearcher = active
        self.numOfPapers = num
        self.highestImpactFactor = hip
        self.example = "researcher"
    def x(self):
        print("I am Researcher")

class Employee:                
    def __init__(self,name,id):
        self.name = name 
        self.id   = id

class Teacher(Employee):
    def __init__(self,name,id,dptName,dptId):
        super().__init__(name,id)
        self.deptName = dptName
        self.deptId = dptId
        self.example = "teacher"
    def x(self):
        print("Teacher")
    
# # # Multi-level Inheritence
# # # Multiple Inheritence
class Professor(Researcher,Teacher):
    def __init__(self, name, id, dptName, dptId,exp,active,num,hip):
        Teacher.__init__(self,name, id, dptName, dptId)
        Researcher.__init__(self,active,num,hip)
        self.designation = "Professor"
        self.experience = exp 
   
class Admin(Employee):
    def __init__(self,name,id,dptName,dptId):
        Employee.__init__(self,name,id)
        self.deptName = ""
        self.deptId = ""


aniq = Teacher("Anique",1,"CS", 51)

gohar = Admin("Gohar",100,"Admisson",27)

aasia = Professor("Aasia",2,"Cs",51,15,True,15,6.7)

print(aasia.experience)

aasia.x()

print(aasia.example)

# ## MRO Method Resolution Order
