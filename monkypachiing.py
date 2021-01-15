#monkypaching...
class A:
    def fetchdata(self):
        print('fatch data from database')
    def getdata(self):
        self.fetchdata()
        print('use data')
        
obj =A()
# obj.getdata()
def testdata():
    print('this is test data')
obj.fetchdata =testdata
obj.getdata()
