class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("i can bark")

class Snake(Animal):
    def move(self):
        print("i can hisss")

obj1 = Dog()
obj2 = Snake()

obj1.move()
obj2.move()

# output  :
#     i can bark
#     i can hisss