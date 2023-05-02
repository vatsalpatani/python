class A:
    def func(self):
        print("class A function")

class B(A):
    def func(self):
        print("class B function")
        super().func()

c1 = B()
c1.func()

# output  :
#     class B function
#     class A function