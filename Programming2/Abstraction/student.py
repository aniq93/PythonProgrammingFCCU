class Student:
    #class_id  = 

    # public 
    # private __
    # protected _

    def __init__(self,fname,lname,rnum,department,minor):
        self.__f_name = fname
        self.__l_name = lname
        self.__rollnum = rnum
        self.__dept = department
        self.__minor = minor
        
        
    def __capital(name):
        upcase = name.upper()
        return upcase    

    def fullname(self):
        fullname = self.__f_name + " " + self.__l_name
        x = Student.__capital(fullname)
        return x

    # getter accesor

    def get_f_name(self):

        return self.__f_name

    # setter, Mutator   

    def set_f_name(self,name):
        self.__f_name = name 




     

