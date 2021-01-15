#encepsulation--
#in encapsulation we can make a class method and data members for a one particular class..and make it privert.
#so cant directly we axiex this data member and method outside the class...
#this method and data member use only for a that particular class...
#1)privert..
#2)pablic..
class A():
    q =110
    def __init__(self,name,sarname):
        __Q =9
        self.__Q =__Q
        print('in a')
        self.name =name
        self.sarname =sarname
    def Studentdata(self):
        r =10
        self.r =r
        print(self.name,self.sarname)
        print(self.name)
        print(self.__Q)
   
obj =A('rumit','patel')
obj.Studentdata()
