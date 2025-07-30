#encapsulation - wrapping the data(variables) and methods in a single unit(class)

#access specifiers
##1.public
##2.private
##3.protected

class Demo():
    def __init__(self,a,b):
       self.__a =a     # private => is access in the same same class only
       self._b =b 
       #print(self.__a)  #protected  =>can be access in any class where inheritance is performed
    # __a = 2 # private
    # _b = 4 #protected

class Demo2(Demo):
   def output(self):
      print(self._b)

obj = Demo2(2,3)
obj.output()



##ACCESS MODIFIERS