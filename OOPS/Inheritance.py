#single inheritance
class Parent:
    def fun1(self):
        print("this is parent")
class Child(Parent):
    def fun2(self):
        print("this is child")
obj=Child()
obj.fun2()
obj.fun1()


# multilevel inheritance

class Parent:
    def fun1(self):
        print("this is parent")
class Child(Parent):
    def fun2(self):
        print("this is child")
class GrandChild(Child):
    def fun3(self):
        print("this is GrandChild")
obj=GrandChild()
obj.fun2()
obj.fun1()
obj.fun3()

# multiple inheritance
class Parent1:
    def fun1(self):
        print("this is parent1")
class Parent2:
    def fun2(self):
        print("this is parent")
class Child(Parent1,Parent2):
    def fun3(self):
        print("this is Child")
obj=Child()

obj.fun2()
obj.fun1()
obj.fun3()

# hierarchical inheritance
class Parent:
    def fun1(self):
        print("this is parent")
class Child1(Parent):
    def fun2(self):
        print("this is child1")
class Child2(Parent):
    def fun3(self):
        print("this is Child2")
obj=Child2()
# obj=Child1()
# obj.fun2()
obj.fun1()
obj.fun3()



