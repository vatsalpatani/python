lst = ["hello", "world"]

file = open("file2.txt","w")

file.writelines(lst)

print("file created")

# output  :
#     file created