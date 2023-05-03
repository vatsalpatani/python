class A:
    def __init__(self,a):
        self.a = a #public variable
    
    def show(self):
        print(self.a)

class B(A):
    def __init__(self, b):
        super().__init__(b)
    
    def show1(self):
        print(self.a)


obj = B(10)
obj.show1()

# output  :   10