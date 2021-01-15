#polimorphisum:
#ploy meany many and phylum  meany form ...
#if the variable, method and object perform different behaviare according to the situation
#this is know as a polymorphism

1)overloading
class Rumit():
    print('hello')
    def data(self,b):
        return b
class Jay(Rumit):
    def data(self,a,b):
        return a+b
    
obj =Jay()
obj.data(10)
