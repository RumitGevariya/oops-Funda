#class method
class A:
    a ='rumit patel'
    
    @classmethod
    def printname(cls):
        return cls.a

obj =A()
A.printname()
