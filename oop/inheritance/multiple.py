class A:
    def func1(self):
        print("class A function")

class B:
    def func2(self):
        print("class B function")

class C(A,B):
    def func3(self):
        print("class C function")

c1 = C()
c1.func1()
c1.func2()
c1.func3()

# output  :
#     class A function
#     class B function
#     class C function