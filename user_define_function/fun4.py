def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n-1)
    
a = int(input("enter a number for sum "))
print(f"sum till {a} : ",recursive_sum(a))

# output  :
#     enter a number for sum 10
#     sum till 10 :  55