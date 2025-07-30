#---abstraction
#@abstarct class => it contains both abstract methods and normal method
#hiding of data

#abc =>abstract base class
from abc import ABC,abstractmethod ;
class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        print("i have any number of sides")


class Triangle(Polygon):
    def __init__(self):
        pass
    def no_of_sides(self):
        print("i have 3 sides")
class Rectangle(Polygon):
    def __init__(self):
        pass
    def no_of_sides(self):
        print("i have 4 sides")         
obj1 = Triangle()
obj2 = Rectangle()
obj1.no_of_sides()
obj2.no_of_sides()