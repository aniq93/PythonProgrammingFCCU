class Person:
    
    def __init__(self,f_name,l_name,gender,age):
        self.first_name = f_name
        self.last_name = l_name
        self.gender = gender
        self.age = age
        self.__cc = ""
    
    def fullname(self):
        name = self.first_name+ " " + self.last_name
        return name

    def future_age(self,x):
        x = self.age + x
        return x
    
    def set_cc(self,card_num):
        self.__cc = card_num 

    def get_cc(self):
        return self.__cc

    
