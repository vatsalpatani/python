try:
    a = int(input("enter a number : "))
    b = int(input("enter 2nd number : "))
except:
    print("this number is not integer")
else:
    sum = a+b
finally:
    print("sum of number : ",sum)
    

# output  :
#     enter a number : 5
#     enter 2nd number : 8
#     sum of number :  13