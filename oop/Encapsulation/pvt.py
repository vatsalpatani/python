class A:
    def __init__(self,a):
        self.__a = a #private variable
    
    def show(self):
        print(self.__a)

class B(A):
    def __init__(self, b):
        super().__init__(b)
    
    def show1(self):
        print(self.__a)


obj = B(10)
obj.show1()

# output  :   AttributeError: 'B' object has no attribute '_B__a'. 
#               # because of private variable