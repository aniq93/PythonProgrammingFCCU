class Person:

    def __init__(self,fname,lname,age):
        #first_name
        self.first_name = fname  #private
        #last_name
        self.last_name = lname
        #age
        self.age  = age
        # 
        self.__credit_card = 0

    def display_properties(self):
        
        print(f"{self.first_name} {self.last_name} {self.age} {self.__credit_card}")

   
    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self,new_first_name):
        self.first_name  = new_first_name
    
    def __make_payment(self):
        print(f"{self.__credit_card} points are deducted")
    
    def set_credit_card(self,cc):
        self.__credit_card = cc

    def get_credit_card(self):
        return self.__credit_card
    def get_on_slot(self):
        x = 20 
        y = x*2
        self.first_name = "Ram"
        self.last_name  = "On Scene"
        
        return self.__make_payment()
    






    '''
     
    getters  setters
    accesors mutator
         public
    _    protected
    __   private
    
    '''
    