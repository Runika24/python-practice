
#super keyword
class A:
    def __init__(self):
        print("this is Class A")
    def fun1(self):
        print("this is Father Class")
class B(A):
    def fun1(self):
        print("this is Class B")
        super().__init__()
    def fun2(self):
        print("this is Mother Class")

obj = B()
# obj.fun1()