#polymorphism - multiple forms or more than one form

#complile-time(method overloading):
#=>same function_name or method_name or same class
#different parameters
#to overcome this method overloading we should write default aurguments
class A:
    def display(self,a,b):
        return a+b
    def display(self,a,b,c=1):
        return a+b+c
obj = A()
print(obj.display(1,3,4))    

#run-time (method over riding):

class A:
    def display(self):
        print("this is class A")
class B(A):
    def display(self):
        print("this is class B")
        super().display()  ###this is used to overcome method over riding
obj=B()
obj.display()                
