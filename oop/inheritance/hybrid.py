class A:
    def func1(self):
        print("class A function")

class B(A):
    def func2(self):
        print("class B function")

class C(A):
    def func3(self):
        print("class C function")

class D(B,C):
    def func4(self):
        print("class D function")

c1 = D()
c1.func1()
c1.func2()
c1.func3()
c1.func4()

# output  :
#     class A function
#     class B function
#     class C function
#     class D function