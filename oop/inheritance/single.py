class ParentClass:
    def func1(self):
        print("this is parentclass function")

class ChildClass(ParentClass):
    def func2(self):
        print("this is childclass function")

c1 = ChildClass()
c1.func1()
c1.func2()


# output  :
#     this is parentclass function
#     this is childclass function