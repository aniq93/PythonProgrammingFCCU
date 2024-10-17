class Doctor:                         # class defination

    def __init__(self , name , age):
        self.doctor_name  = name      #instance variables
        self.doctor_age  = age

    def show_name(self):
        print(self.doctor_name)

    
doctors_list  = []

for i in range(2):
    name = input("Enter Name")
    age  = input("Enter age")
    doctors_list.append(Doctor(name , age))

for i in doctors_list:
    print(i.doctor_name , i.doctor_age)

print(doctors_list)