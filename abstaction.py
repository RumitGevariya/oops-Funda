#abstraction...

# data Abstract

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def halfarea(self):
        pass
    
class circul(shape):
    def __init__(self,r):
        self.r =r
    def area(self):
        return 3.14*self.r*self.r
    def halfarea(self):
        return ((3.14*self.r*self.r)/4)
    
obj =circul(5)
obj.area()
obj.halfarea()
