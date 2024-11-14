class Doctor: 

    raise_amount = 1.04 
                          
 # class defination

    def __init__(self , name:str , age:int, pay:float):
        self.doctor_name  = name      #instance variables
        self.doctor_age  = age
        self.doctor_pay = pay    

    def pay_raise(self) :
        self.doctor_pay = int(self.doctor_pay * Doctor.raise_amount)


    def __repr__(self) -> str:
        return f"Doctor Name:{self.doctor_name} , Doctor Age:{self.doctor_age} , Doctor Pay:{self.doctor_pay}"
    
    
doc1 = Doctor('anique' , 40 , 40000)
doc2 = Doctor('zanib' , 30 , 450000)
doc3 = Doctor('Ajay' , 32 , 450000)
doc4 = Doctor('Dimple' , 36 , 450000)


doc1.pay_raise()
# print(doc1.doctor_pay)

doc2.pay_raise()
# print(doc2.doctor_pay)

# print (doc1)
x = doc1.__dict__

print(x["doctor_age"])

# print(doc2.__dict__)

# print(Doctor.__dict__)
# doctors_list  = []

# for i in range(2):
#     name = input("Enter Name")
#     age  = input("Enter age")
#     doctors_list.append(Doctor(name , age))

# for i in doctors_list:
#     print(i.doctor_name , i.doctor_age)

# print(doctors_list)