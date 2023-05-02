class A:
    
    def func(self):
        print("function with no argument")

    def func(self,a):
        print("function with 1 argument")

    def func(self,a,b):
        print("funtion with 2 argument")

obj = A()

obj.func(1,1)

# note    :
#     as python is a interpreted language so hear method 
#       overloading is not supported

# output  :
#     funtion with 2 argument