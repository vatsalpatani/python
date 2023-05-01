lst1 = [1,2,3,4,5]
lst2 = ['a','b','c','d','e']

dict = {}

for i in range(len(lst1)):
  dict[lst1[i]] = lst2[i]

print("The dictionary is: ",dict)

# output  :
#     The dictionary is:  {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}