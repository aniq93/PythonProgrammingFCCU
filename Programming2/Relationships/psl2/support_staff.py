class SupportStaff:

    def __init__(self, name ,id, desg ,exp):

        self.name = name
        self.id = id
        self.designation = desg
        self.experince = exp
    
    def display_support_staff_properties(self):

        print(self.name ,self.id ,self.designation , self.experince)