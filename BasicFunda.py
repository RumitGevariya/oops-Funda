class myinfo():
    def __init__(self,name,age):
        #print("hi")
        self.z =10
        self.name =name
        self.age =age
    
    def info(self,a,k,c):
        self.a =a
        self.k =k
        self.c =100
        return a,k
    def person(self):
        return self.a
    def people(self):
        return self.a
    def print(self):
        return self.name ,self.age
    
    
#dynemic input    
'''while True: 
    i =input("what is you name.")
    j =int(input("what is your age??"))
    obj1 =myinfo(i,j)
    print(obj1.print())
'''

l1 ={'rumit':21,'abhay':22,'vishal':20,'jay':19}
for i,j in l1.items():
    obj1 =myinfo(i,j)
    print(obj1.print())
#obj1 =myinfo() 
#obj1 =myinfo("abhay",22)
#obj =myinfo("naman",21)
#obj1 =myinfo("rumit",20)
#print(obj.print())
#print(obj1.print())
#obj.info(10,20,60)
#print(obj.person())
#print(obj.people())
#print(type(obj))
#print(obj.info(10,20))
#print(obj.people())
