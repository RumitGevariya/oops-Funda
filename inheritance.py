#class 
#how the class created?
#inheritance allow you to defind a class that inheriuse the class proparety and method pf the other class

class A():
    def __init__(self,name,sarname):
        print('in a')
        self.name =name
        self.sarname =sarname
    def Studentdata(self):
        print(self.name,self.sarname)
       
    
class B(A):
    def __init__(self,name,sarname,age):
        print('in b')
        self.age =age
        super().__init__(name,sarname)
    def studentfulldata(self):
        print(self.name,self.sarname)
        

class C(B):
    def studentcontact(self,contact):
        print(self.name,self.sarname,self.age,contact)
ob =C('rumit','patel','22')
# ob.studentcontact('95859')
# ob.studentfulldata()
# ob.Studentdata()
