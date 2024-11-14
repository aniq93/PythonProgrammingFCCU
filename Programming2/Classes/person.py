class Person:

    def __init__(self,f_name,l_name,gender,age , cc):
        self.first_name = f_name
        self.last_name = l_name
        self.gender = gender
        self.__age = age
        self.__cc = cc

    
    
    def fullname(self):
        name = self.first_name+ " " + self.last_name
        return name

    def future_age(self,x):
        x = self.age + x
        return x
    def get_cc(self):
        return self.__cc
    
    @property
    def cc(self):
        return self.__cc
    
    @cc.setter
    def cc(self,x):
        self.__cc = x

    
