s = "this is new text of file"
file = open("file1.txt","a")
file.write(s)
print("file updated")
file.close()

# output  :
#     file updated