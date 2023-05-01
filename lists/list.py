n = int(input("Enter the number of elements in the list: "))

lst = []

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    lst.append(element)

print(f"The list is: {lst}")

print("The alternate elements are: ")
for i in range(0, n):
  print(lst[i])

# output  :
    # Enter the number of elements in the list: 5
    # Enter element 1: 4
    # Enter element 2: 8
    # Enter element 3: 5
    # Enter element 4: 6
    # Enter element 5: 9
    # The list is: ['4', '8', '5', '6', '9']
    # The alternate elements are:
    # 4
    # 8
    # 5
    # 6
    # 9