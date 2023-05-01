try:
    print(c)
except NameError as e:
    print("variable not define")
except:
    print("exception")

# output  :
#     variable not define