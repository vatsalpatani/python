class A:
    def __init__(self,a):
        self._a = a #protected variable
    
    def show(self):
        print(self._a)

class B(A):
    def __init__(self, b):
        super().__init__(b)
    
    def show1(self):
        print(self._a)


obj = B(10)
obj.show1()

# output  :   10