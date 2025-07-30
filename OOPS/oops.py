#encapsulation : hidding sennsitive data(binding of data using of methods is encapsulation) 
#  
##deppendency
# access specifiers : 3 types
#                   i) private    ( '__' is added in front of the variable)
#                  ii) public             iii) protected 
#
class HumanBeing:
    def __init__(self,name,age):
        self.name =name
        self.age = int(age)
#setters,getters(accessers,modifiers):

##setters=> method used to retrieve (get ) the value of a private attributes.
##getters =>method used to set or update the value of a private attribute .
    #getters method
    def get_name(self):
        return self.name  
    def get_age(self):
        return self.age  
    #setter method
    def set_name(self,new_name):
        self.name = new_name  
    def set_age(self,new_age):
        self.age = new_age 
    def set_age(self, new_age):
        if new_age >= 0:    # Validation
            self.age = new_age
        else:
            print("Age cannot be negative")        
hm1 = HumanBeing('Person1',32)
hm2 = HumanBeing('Person2',64)

# print(hm1.name)
print(hm1.get_name())
hm1.set_name('person3')
print(hm1.get_name())


# abstraction  :  hides implimentation details of methods. 
# abstract class => 
# abstract methods : represented by @abstractmethod 
